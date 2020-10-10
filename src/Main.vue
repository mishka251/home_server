<template>
    <div>

        <BooksList
        get-items-url="/api/v1/books/"
        put-item-url="/api/v1/books/"
        ></BooksList>
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from 'vue-property-decorator';
import BooksList from './BooksList.vue';
    @Component({
        components:{
            BooksList,
        }
    })
    export default class Main extends Vue {

    };
</script>

<style scoped>

</style>