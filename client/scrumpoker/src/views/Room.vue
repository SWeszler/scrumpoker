<template>
    <div>
        room
        {{ activeUsers }}
    </div>
</template>

<script lang="ts">
import { defineComponent, reactive, toRefs } from 'vue';

export default defineComponent({
  setup(){
    const compData = reactive({
      activeUsers: ["test"]
    });

    return { ...toRefs(compData) };
  }
});
</script>