<template>
    <div>
        <div
                v-if="possibleValues!=null"
                :class="sizeClasses">
            <!--      <div ref="prependDiv" v-if="$slots.prepend || prepend" class="input-group-prepend">-->
            <!--        <slot name="prepend">-->
            <!--          <span class="input-group-text">{{ prepend }}</span>-->
            <!--        </slot>-->
            <!--      </div>-->
            <input
                    ref="input"
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
            <!--      <div v-if="$slots.append || append" class="input-group-append">-->
            <!--        <slot name="append">-->
            <!--          <span class="input-group-text">{{ append }}</span>-->
            <!--        </slot>-->
            <!--      </div>-->
        </div>
        <List
                class="vbt-autcomplete-list"
                ref="list"
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

    get placeholder():string{
        if(this._value){
            return this._value.caption;
        }
        return this.label;
    }

    @Prop()
    backgroundVariant!:string;

    @Prop()
    textVariant!:string;

    get sizeClasses() {
        return this.size ? `input-group input-group-${this.size}` : 'input-group'
    }

    isFocused = false;
    inputValue = '';

    // resizeList(el:any) {
    //     const rect = el.getBoundingClientRect()
    //     const listStyle = this.$refs.list.$el.style
    //     // Set the width of the list on resize
    //     listStyle.width = rect.width + 'px'
    //     // Set the margin when the prepend prop or slot is populated
    //     // (setting the "left" CSS property doesn't work)
    //     if (this.$refs.prependDiv) {
    //         const prependRect = this.$refs.prependDiv.getBoundingClientRect()
    //         listStyle.marginLeft = prependRect.width + 'px'
    //     }
    // }

    handleHit(item:Item) {
        // if (typeof this._value !== 'undefined') {
        //     this.$emit('input', evt.text)
        // }
        this.inputValue = item.caption;
        // this.$emit('hit', evt.data)
        this._value = item;
        //this.$refs.input.blur()
        this.isFocused = false
    }

    handleBlur(evt:any) {
        const tgt = evt.relatedTarget
        if (tgt && tgt.classList.contains('vbst-item')) {
            return
        }
        this.isFocused = false
    }

    handleInput(newValue:string) {
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