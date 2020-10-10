<template>
<div>
    <div>
        <label for="name">Название</label>
        <input type="text" name="name" id="name" v-model="name">
    </div>
</div>
</template>

<script lang="ts">
import { Component, Prop, Vue, Ref } from 'vue-property-decorator';
// import { BTable, BTooltip, BvTableFieldArray } from 'bootstrap-vue';
import axios, { AxiosError, AxiosResponse } from 'axios';

@Component
export default class Book extends Vue {
name:string='';

}
</script>

<style scoped>

</style>