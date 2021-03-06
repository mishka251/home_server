<template>
    <div>
        <div
                v-if="possibleValues!=null"
                :class="sizeClasses">

            <input
                    type="search"
                    class="form-control"
                    :placeholder="placeholder"
                    :aria-label="placeholder"
                    :value="inputValue"
                    @focus="isFocused = true"
                    @blur="handleBlur"
                    @input="handleInput($event.target.value)"
                    autocomplete="off"
            />
        </div>
        <List
                class="vbt-autcomplete-list"
                v-show="isFocused && possibleValues.length > 0"
                :query="inputValue"
                :data="possibleValues"
                :background-variant="backgroundVariant"
                :text-variant="textVariant"
                @hit="handleHit"
        >

        </List>
    </div>
</template>

<script lang="ts">
import { Component, Vue, Prop, PropSync, Watch } from 'vue-property-decorator';
import List from "./List.vue";
import Item from "./Item";

import axios, { AxiosResponse } from 'axios';

@Component({
    components: { List },
})
export default class AutoCompleteInput extends Vue {
    @Prop()
    size!: string;

    @PropSync('value')
    _value!: Item | null;

    @Prop({ type: String })
    dataUrl!: string;

    @Prop({ type: String })
    label!: string;

    get placeholder(): string {
        if (this._value) {
            return this._value.caption;
        }
        return this.label;
    }

    @Prop()
    backgroundVariant!: string;

    @Prop()
    textVariant!: string;

    get sizeClasses() {
        return this.size ? `input-group input-group-${this.size}` : 'input-group'
    }

    isFocused = false;
    inputValue = '';


    handleHit(item: Item) {
        this.inputValue = item.caption;
        this._value = item;
        this.isFocused = false
    }

    handleBlur(evt: any) {
        const tgt = evt.relatedTarget
        if (tgt && tgt.classList.contains('vbst-item')) {
            return
        }
        this.isFocused = false
    }

    handleInput(newValue: string) {
        this.inputValue = newValue
        // If v-model is being used, emit an input event
        if (typeof this._value !== 'undefined') {
            this.$emit('input', newValue)
        }
    }

    possibleValues: Item[] | null = null;


    @Watch('inputValue', {
        immediate: true,
    })
    loadData(): void {
        axios.get(this.dataUrl, {
            params: {
                search: this.inputValue,
            },
        })
                .then((result: AxiosResponse<Item[]>) => {
                    this.possibleValues = result.data;
                })

    }


}
</script>

<style scoped>

</style>