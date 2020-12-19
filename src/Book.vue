<template>
<div>
    <div v-if="isLoaded">
        <div>
            Автор
<!--            <a :href="'/authors/'+book.author.id">{{ book.author.__str__ }}</a>-->
            <AutoCompleteInput
            label="Автор"
            data-url="/api/v1/authors/autocomplete/"
            :value.sync="book.author"
            ></AutoCompleteInput>
        </div>
        <div>
            Жанры
            <AutoCompleteInputMulti
            label="Жанры"
            data-url="/api/v1/genres/autocomplete/"
            :value.sync="book.genres"
            >

            </AutoCompleteInputMulti>
        </div>
        <div>
            <label for="name">Название</label>
            <input type="text" name="name" id="name" v-model="book.name">
        </div>
          <div>
            <label for="publish_year">Год издания</label>
            <input type="number" name="publish_year" id="publish_year" v-model="book.publish_year">
        </div>
          <div>
            <label for="size">Размер (кб)</label>
            <input type="number" name="size" id="size" v-model="book.size">
        </div>

    </div>

</div>
</template>

<script lang="ts">
import { Component, Prop, Vue, Ref } from 'vue-property-decorator';
// import { BTable, BTooltip, BvTableFieldArray } from 'bootstrap-vue';
import axios, { AxiosError, AxiosResponse } from 'axios';
import AutoCompleteField from "./AutoCompleteField.vue";
import AutoCompleteInput from "./Autocomplete/AutoCompleteInput.vue";
import AutoCompleteInputMulti from './Autocomplete/AutoCompleteInputMulti.vue';

interface Book{
    id: number;
    author: {
        __str__:string;
        id:number;
    };
    file: string|null;
    file_type:string|null;
    genres:number[];
    name: string;
    publish_year:number;
    size: number|null;
}

@Component({
    components:{
        AutoCompleteInput,
        AutoCompleteInputMulti,
    }
})
export default class BookPage extends Vue {
 @Prop({ type: Number, required: true })
    bookId!: number;

  book: Book | null = null;
    isLoaded: boolean = false;

        mounted() {
        this.loadBook();
    }

    loadBook() {
        this.isLoaded = false;
        axios.get(`/api/v1/books/${this.bookId}/`)
                .then((response: AxiosResponse<Book>) => {
                    console.log('response', response);
                   // this.name = response.data.name;
                  //  this.surname = response.data.surname;
                    this.book = response.data;
                    this.isLoaded = true;
                })
    }

    save(): void {
        this.isLoaded = false;
        axios.put(`/api/v1/books/${this.bookId}/`, this.book)
                .then((response: AxiosResponse<Book>) => {
                    console.log('response', response);
                    // this.name = response.data.name;
                    // this.surname = response.data.surname;
                    this.book = response.data;
                    this.isLoaded = true;
                })
    }
}
</script>

<style scoped>

</style>