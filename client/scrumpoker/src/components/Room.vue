<template>
  <div class="bg-red-200 p-1">
    <div>{{ players }}</div>
    <textarea class="bg-transparent" v-model="output"></textarea>
    <input class="border-black rounded shadow" v-model="playerName"/>
    <button class="border-black rounded p-1" @click="startGame">Start</button>
    <input class="border-black rounded shadow" v-model="message"/>
    <button class="border-black rounded p-1" @click="sendMsg">Send</button>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';

@Options({
  name: 'Room'
})

export default class Room extends Vue {
  ws: WebSocket = new WebSocket('ws://localhost:5000/ws/join-game/');
  output: string = '';
  message: string = '';
  playerName: string = '';
  players: string[] = [];

  created(){
    this.ws.onmessage = (e) => {
      const data = JSON.parse(e.data);
      this.output += data.message + '\n';
      this.players.push(data.player);
    }
  }

  sendMsg(){
    this.ws.send(JSON.stringify({
      'player': this.playerName,
      'message': this.message
    }));
  }

  startGame(){
    this.ws.send(JSON.stringify({
      'player': this.playerName,
      'message': ''
    }));
  }
}
</script>

<style scoped>
</style>
