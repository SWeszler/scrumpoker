<template>
  <div>
    <div v-if="loading">
      Loading...
    </div>
    <div v-else >
      {{ activeUsers }}
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, toRefs } from "vue";
import { useStore } from "vuex";

const WS_URL = process.env.VUE_APP_WS_URL;

export default defineComponent({
  setup(){
    const compData = reactive({
      activeUsers: [] as string[],
      loading: true as boolean
    });
    const store = useStore();

    const ws = new WebSocket(
      WS_URL + "ws/join-game/" + "?token=" + store.state.accessToken
    );
    ws.onmessage = e => {
      const data = JSON.parse(e.data);
      console.log(data);
      compData.activeUsers = data.players;
      compData.loading = false;
    }

    return { ...toRefs(compData) };
  }
});
</script>