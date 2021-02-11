<template>
    <div>
        room
        {{ activeUsers }}
    </div>
</template>

<script lang="ts">
import { defineComponent, reactive, toRefs } from 'vue';
const WS_URL = process.env.VUE_APP_WS_URL;

export default defineComponent({
  setup(){
    const compData = reactive({
      activeUsers: ["test"]
    });

    const ws = new WebSocket(WS_URL + 'ws/join-game/');
    ws.onmessage = (e) => {
      const data = JSON.parse(e.data);
      console.log(data);
      compData.activeUsers = data.players;
    }

    return { ...toRefs(compData) };
  }
});
</script>