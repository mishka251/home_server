import AuthorPage from "./AuthorPage.vue";

document.addEventListener('DOMContentLoaded', () => {
    //console.log('hello ');
    const authorId:string|undefined = document
        .getElementById('vue-main')
        ?.attributes
        ?.getNamedItem('data-id')
        ?.value;
    new AuthorPage({
        el: '#vue-main',
        propsData:{
            authorId:+(authorId||'1'),
        }
    });
});