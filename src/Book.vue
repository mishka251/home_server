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
            <label for="name">Название</label>
            <input type="text" name="name" id="name" v-model="book.name">
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