<template>
  <div class="bg-red-200 p-1">
    <textarea class="bg-transparent" v-model="output"></textarea>
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
  ws: WebSocket = new WebSocket('ws://localhost:5000/ws/pol-data/');
  output: string = '';
  message: string = '';

  created(){
    this.ws.onmessage = (e) => {
      const data = JSON.parse(e.data);
      this.output += data.message + '\n';
    }
  }

  sendMsg(){
    this.ws.send(JSON.stringify({
      'message': this.message
    }));
  }
}
</script>

<style scoped>
</style>
