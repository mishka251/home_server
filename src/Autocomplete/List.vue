<template>
<div class="list-group shadow">
    <ListItem
      v-for="(item, id) in data"
      :key="id"
      :data="item"
      :background-variant="backgroundVariant"
      :text-variant="textVariant"
      @click="handleHit"
    >
    </ListItem>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop, Emit } from 'vue-property-decorator';
import ListItem from "./ListItem.vue";
import Item from "./Item";


@Component({
    components: { ListItem },
})
export default class List extends Vue {
    @Prop({type:Array})
    data!: Item[];

        @Prop({ type: String })
    textVariant!: string;

            @Prop({ type: String })
    backgroundVariant!: string;

    @Emit('hit')
     handleHit(item:Item) {
      return item;
    }
  }

</script>