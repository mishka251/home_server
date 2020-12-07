<template>
    <div>
        <label>{{ label }}</label>
        <input type="text" v-model="valueCaption" @click="showAutocomplete">

        <div class="autocomplete-form">
            <input type="text" name ="filter" v-model="searchValue">
            <div>
                <ul>
                    <li v-for="option in options"
                    :key="option.id"
                    @click="selectOption(option)">
                        {{option.caption}}
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue, Ref, PropSync } from 'vue-property-decorator';
// import { BTable, BTooltip, BvTableFieldArray } from 'bootstrap-vue';
import axios, { AxiosError, AxiosResponse } from 'axios';

interface Option {
    id: number;
    caption: string;
}

export default class AutoCompleteField extends Vue {

    @Prop({ type: String, required: true })
    dataUrl!: string;

    @Prop({ type: String, required: true })
    label!: string;

    searchValue: string = '';

    options: Option[] = [];

    @PropSync('value')
    _value!: Option | null;

    isVisible:boolean=false;

    get valueCaption(): string {
        return this._value ? this._value.caption : '';
    }

    getOptions() {
        axios.get(this.dataUrl, {
            params: {
                search: this.searchValue,
            },
        })
                .then((result: AxiosResponse<Option[]>) => {
                    this.options = result.data;
                })
    }
    showAutocomplete():void{
        this.isVisible=true;
    }
    hideAutocomplete():void{
        this.isVisible=false;
    }

    selectOption(option:Option):void{
        this._value=option;
        this.hideAutocomplete();
    }
}
</script>

<style scoped>

</style>