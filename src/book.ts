import BookPage from "./Book.vue";
require('./main.scss');

document.addEventListener('DOMContentLoaded', () => {
    //console.log('hello ');
    const bookId:string|undefined = document
        .getElementById('vue-main')
        ?.attributes
        ?.getNamedItem('data-id')
        ?.value;
    new BookPage({
        el: '#vue-main',
        propsData:{
            bookId:+(bookId||'1'),
        }
    });
});