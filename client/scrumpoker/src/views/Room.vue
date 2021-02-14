<template>
  <div class="grid grid-cols-1 md:grid-cols-2">
    <div>
      <div v-if="loading">
        Loading...
      </div>
      <div v-else>
        <ul>
          <li v-for="(player, index) in activeUsers" :key="index">
            <span>{{index + 1}}. {{player.name}}</span>
            <span class="ml-5" v-if="player.vote > 0" v-text="player.vote"></span>
            <span v-else></span>
          </li>
        </ul>
      </div>
    </div>
    <div>
      <div>
        <button @click="flipCards" class="p-2 rounded bg-black">Flip Cards</button>
      </div>
      <div class="p-5">
        <ul class="flex">
          <li class="mr-5" v-for="card in cards" :key="card">
            <button class="p-3 border border-gray-400 rounded" @click="vote(card)" v-text="card"></button>
          </li>
        </ul>
      </div>
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
      const data = {
        vote: cardVote
      }
      ws.send(JSON.stringify(data));
    }

    function flipCards(){
      console.log("flippin...");
    }

    return { ...toRefs(compData), vote, flipCards };
  }
});
</script>
