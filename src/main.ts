import Main from './Main.vue';
require('./main.scss');
document.addEventListener('DOMContentLoaded', () => {
    //console.log('hello ');
    new Main({
        el: '#vue-main',
    });
});