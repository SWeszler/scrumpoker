<template>
  <div>
    <textarea v-model="output"></textarea>
    <input v-model="message"/>
    <button @click="sendMsg">Send</button>
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
