<template>
    <button
            class="vbst-item list-group-item list-group-item-action"
            :class="textClasses"
            @mouseover="active = true"
            @mouseout="active = false"
            @click="onClick"
    >
        <span> {{ data.caption }}</span>
    </button>
</template>

<script lang="ts">

import { Component, Prop, Vue, Emit } from 'vue-property-decorator';
import Item from "./Item";

@Component({})
export default class ListItem extends Vue {
    @Prop()
    data!: Item;

    @Prop({ type: String })
    backgroundVariant!: string;

    @Prop({ type: String })
    textVariant!: string;


    active = false;

    get textClasses(): string {
        let classes = ''
        classes += this.active ? 'active' : ''
        classes += this.backgroundVariant ? ` bg-${this.backgroundVariant}` : ''
        classes += this.textVariant ? ` text-${this.textVariant}` : ''
        return `${classes}`
    }

    @Emit('click')
    onClick() {
        console.log('click');
        return this.data;
    }
}
</script>
