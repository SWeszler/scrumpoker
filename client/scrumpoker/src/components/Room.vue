<template>
  <div>
    <div>{{ players }}</div>
    <input class="border-black rounded shadow" v-model="playerName"/>
    <button class="border-black rounded p-1" @click="joinGame">Join Game</button>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';

@Options({
  name: 'Room'
})

export default class Room extends Vue {
  ws: WebSocket = new WebSocket('ws://localhost:5000/ws/join-game/');
  playerName: string = '';
  players: {[name: string]: {}} = {'' : {}};

  created(){
    this.ws.onmessage = (e) => {
      const data = JSON.parse(e.data);
      console.log(data);
      this.players = data.players;
    }
  }

  joinGame(){
    this.ws.send(JSON.stringify({
      'player': this.playerName
    }));
  }
}
</script>

<style scoped>
</style>
