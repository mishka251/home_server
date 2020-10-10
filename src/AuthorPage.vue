<template>
    <div>
        <div>Автор</div>
        <div>
            <label
                    for="name">
                Имя
            </label>
            <input type="text" id="name" name="name"
                   v-model="name">
        </div>
        <div>
            <label
                    for="surname">
                Фамилия
            </label>
            <input type="text" id="surname" name="surname"
                   v-model="surname">
        </div>
        <div v-if="hasChanges">
            <button
                    @click="save">
                Сохранить
            </button>
        </div>

        <div>
            Книги автора
            <BooksList
                    get-items-url="/api/v1/books/"
                    put-item-url="/api/v1/books/"
                    :author="authorId"
            ></BooksList>
        </div>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue, Ref } from 'vue-property-decorator';
// import { BTable, BTooltip, BvTableFieldArray } from 'bootstrap-vue';
import axios, { AxiosError, AxiosResponse } from 'axios';
import BooksList from "./BooksList.vue";

interface Author {
    name: string;
    surname: string;
}

@Component({
    components: {
        BooksList,
    },
})
export default class AuthorPage extends Vue {
    name: string = '';
    surname: string = '';

    @Prop({ type: Number, required: true })
    authorId!: number;

    author: Author | null = null;
    isLoaded: boolean = false;

    get hasChanges(): boolean {
        return this.isLoaded &&
                (this.name != this.author?.name
                        || this.surname != this.author?.surname);
    }

    mounted() {
        this.loadAuthor();
    }

    loadAuthor() {
        this.isLoaded = false;
        axios.get(`/api/v1/authors/${this.authorId}/`)
                .then((response: AxiosResponse<Author>) => {
                    console.log('response', response);
                    this.name = response.data.name;
                    this.surname = response.data.surname;
                    this.author = response.data;
                    this.isLoaded = true;
                })
    }

    save(): void {
        this.isLoaded = false;
        axios.put(`/api/v1/authors/${this.authorId}/`, {
            name: this.name,
            surname: this.surname,
        })
                .then((response: AxiosResponse<Author>) => {
                    console.log('response', response);
                    this.name = response.data.name;
                    this.surname = response.data.surname;
                    this.author = response.data;
                    this.isLoaded = true;
                })
    }
}
</script>

<style scoped>

</style>