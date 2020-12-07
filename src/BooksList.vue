<template>
    <div>
        <div class="d-flex flex-column">
            <div class="d-flex ">
                <div class="align-self-center">
                    <img src="/static/img/cat_search1.jpg" alt="Search">
                </div>
                <div class="align-self-center flex-grow-1 pl-1">
                    <div>
                        <div class="form-group form-label-group float">
                            <input
                                    id="searchbar"
                                    type="text"
                                    size="40"
                                    class="form-control vTextField"
                                    :class="{'placeholder-shown':searchValue==''}"
                                    placeholder="Поиск"
                                    v-model="searchValue"
                            >
                            <label for="searchbar">Поиск</label>
                        </div>
                    </div>
                </div>
                <div class="align-self-center flex-grow-1 pl-1 cursor-pointer">

                    <!--                    <img-->
                    <!--                            ref="tooltipTarget"-->
                    <!--                            src="/static/admin/img/icon-unknown.svg"-->
                    <!--                    >-->
                    <span
                            ref="tooltipTarget">
                        ?
                    </span>
                    <BTooltip
                            v-if="isMounted"
                            placement="right"
                            :target="tooltipTarget">
                        <h6>Поиск по следующим полям:</h6>
                        <div class='dropdown-divider'></div>
                        -TODO
                    </BTooltip>
                </div>
            </div>

        </div>
        <div>
            <BTable
                    :items="items"
                    :fields="fields"
            >
                <template v-slot:cell(name)="data">
                    <span v-if="mobile">
                        <a :href="data.item.file"><i class="fa fa-download"></i></a>
                        <a :href="'/books/'+data.item.id">{{ data.item.name }}</a>
                    </span>
                    <span v-else>{{ data.item.name }}</span>
                </template>
                <template v-slot:cell(author)="data">
                    <a :href="'/authors/'+data.item.author.id">{{ data.item.author['__str__'] }}</a>
                </template>
                <template v-slot:cell(file)="data">
                    <a :href="data.item.file">Скачать</a>
                </template>
                <template v-slot:cell(id)="data">
                    <a :href="'/books/'+data.item.id">Редактировать</a>
                </template>
            </BTable>
        </div>

        <label for="file">Загрузить новые</label>
        <input class="file_box__file" type="file" name="file" id="file"
               @change="onAddFile"/>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue, Ref, Watch } from 'vue-property-decorator';
import { BTable, BTooltip, BvTableFieldArray } from 'bootstrap-vue';
import axios, { AxiosError, AxiosResponse } from 'axios';
import { isMobile } from "./utils.ts";

interface BookInfo {
    author: string;
    name: string;
    file: string;
    file_type: string;
    genres: string[];
    id: number;
    publish_year: number;
}


@Component({
    components: {
        BTable,
        BTooltip,
    },
})
export default class BooksList extends Vue {
    @Prop()
    getItemsUrl!: string;

    @Prop()
    putItemUrl!: string;

    @Prop({ default: () => ['.fb2', '.zip'] })
    possibleFileTypes!: string[];

    @Prop({ default: null, type: Number })
    author!: number;

    get h() {
        return window.innerWidth;
    }

    // @Prop()
    // filters!:any;
    items: BookInfo[] = [];

    searchValue: string = '';
    isMounted: boolean = false;

    @Ref('tooltipTarget')
    tooltipTarget!: HTMLElement;

    get mobile(): boolean {
        return isMobile();
    }

    get fields(): BvTableFieldArray {
        let fields = [
            {
                key: 'name',
                label: 'Название',
            },
            {
                key: 'author',
                label: 'Автор',
            },
        ];
        console.log(isMobile());
        if (!isMobile()) {
            fields = [
                ...fields,
                {
                    key: 'file_type',
                    label: 'Формат',
                },
                {
                    key: 'size',
                    label: 'Размер файла (кб)',
                },
                {
                    key: 'file',
                    label: 'Ссылка',
                },
                {
                    key: 'id',
                    label: 'Редактирование',
                },
            ]
        }

        if (this.author != null) {
            delete fields[1];
        }
        return fields;
    }

    mounted(): void {
        this.isMounted = true;
        this.getBooks();
    }

    @Watch('searchValue')
    getBooks() {
        axios.get(this.getItemsUrl, {
            params: {
                name: this.searchValue,
                author: this.author,
            },
        })
                .then((response) => {
                    this.items = response.data;
                })
    }

    onAddFile(e: Event) {
        const input: HTMLInputElement = e.target as HTMLInputElement;

        const files = input.files;
        if (!files) {
            return;
        }
        const file = files[0];

        console.log(file);
        const startIndex = file.name.lastIndexOf('.');
        if (startIndex == -1) {
            alert('Нет типа файла');
            return;
        }
        const extension = file.name.substr(startIndex, file.name.length);
        console.log(extension);
        if (this.possibleFileTypes.indexOf(extension) == -1) {
            alert('Неверный тип файла');
            return;
        }
        this.loadBook(file);
    }

    loadBook(file: File) {
        const formData = new FormData();
        formData.append("file", file);
        axios.post('/api/v1/upload/', formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        })
                .then((response: AxiosResponse<BookInfo[]>) => {
                    console.log(response);
                    this.items = [
                        ...this.items,
                        ...response.data,
                    ];
                })
                .catch((error: AxiosError) => {
                    console.error(error);
                    if (error.code == '403') {
                        alert('Залогинься');
                    }
                });
    }
}
</script>

<style scoped>

</style>