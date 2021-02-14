<template>
  <div>
    <div v-if="loading">
      Loading...
    </div>
    <div v-else>
      {{ activeUsers }}
    </div>
    <div class="p-5">
      <ul class="flex">
        <li v-for="card in cards" :key="card">
          <button class="p-3 border-black" @click="vote(card)" v-text="card"></button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, toRefs } from "vue";
import { useStore } from "vuex";

const WS_URL = process.env.VUE_APP_WS_URL;

export default defineComponent({
  setup() {
    const compData = reactive({
      activeUsers: [] as string[],
      loading: true as boolean,
      cards: [1, 2, 3, 5, 8]
    });
    const store = useStore();

    const ws = new WebSocket(
      WS_URL + "ws/join-game/" + "?token=" + store.state.accessToken
    );
    ws.onmessage = e => {
      const data = JSON.parse(e.data);
      compData.activeUsers = data.players;
      compData.loading = false;
    };

    function vote(cardVote: number){
      console.log("my vote:",cardVote);
      const data = {
        vote: cardVote
      }
      ws.send(JSON.stringify(data));
    }

    return { ...toRefs(compData), vote };
  }
});
</script>
