<template>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
    <div>
      <div v-if="loading">
        Loading...
      </div>
      <div v-else>
        <ul class="bg-white rounded shadow-md p-5">
          <li v-for="(player, index) in activeUsers" :key="index">
            <span class="mr-5">{{ index + 1 }}. {{ player.name }}</span>
            <span v-if="allVoted" v-text="player.vote"></span>
            <span class="text-green-400" v-else-if="player.voted"
              ><i class="far fa-check-circle"></i
            ></span>
            <span v-else><i class="fas fa-hourglass-half"></i></span>
          </li>
        </ul>
      </div>
    </div>
    <div class="col-span-2">
      <div class="mb-10">
        <button
          @click="restartGame"
          class="focus:outline-none hover:bg-gray-400 pt-1 pb-1 pr-3 pl-3 shadow-md rounded-full bg-gray-300"
        >
          Restart
        </button>
      </div>
      <div>
        <ul class="flex flex-wrap">
          <li class="mr-5 mb-5" v-for="card in cards" :key="card">
            <button
              class="p-5 border border-gray-400 rounded bg-white shadow-md"
              @click="vote(card)"
              v-text="card"
              :disabled="allVoted"
            ></button>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, toRefs, computed } from "vue";
import { useStore } from "vuex";
import { Player } from "@/types";

const WS_URL = process.env.VUE_APP_WS_URL;

export default defineComponent({
  setup() {
    const compData = reactive({
      activeUsers: [] as Player[],
      loading: true as boolean,
      cards: [1, 2, 3, 5, 8, 13, 20, 40, 100]
    });
    const store = useStore();
    const allVoted = computed(() => {
      let result = true;
      compData.activeUsers.forEach(player => {
        if (!player.voted) {
          result = false;
        }
      });
      return result;
    });

    const ws = new WebSocket(
      WS_URL + "ws/join-game/" + "?token=" + store.state.accessToken
    );
    ws.onmessage = e => {
      const data = JSON.parse(e.data);
      compData.activeUsers = data.players;
      compData.loading = false;
    };

    function vote(cardVote: number) {
      const data = {
        vote: cardVote
      };
      ws.send(JSON.stringify(data));
    }

    function restartGame() {
      const data = {
        restart: true
      };
      ws.send(JSON.stringify(data));
    }

    return { ...toRefs(compData), vote, restartGame, allVoted };
  }
});
</script>
