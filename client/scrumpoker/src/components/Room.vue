<template>
  <div>
    <textarea v-model="thread"></textarea>
    <input v-model="message" type="text" />
    <button @click="sendMsg">Send</button>
  </div>
</template>

<script lang="ts">
import { Vue } from 'vue-class-component';

export default class Room extends Vue {
  // thread: string = 'start\n';
  // message: string;
  // ws: WebSocket;

  data(){
    return {
      ws: false,
      thread: false,
      message: false,
    }
  }

  // created() {
  //   this.ws = new WebSocket('ws://localhost:5000/ws/pol-data/');
  //   this.ws.onmessage = (e) => {
  //     const data = JSON.parse(e.data);
  //     this.thread += data.message + '\n';
  //   };
  // }

  // sendMsg() {
  //   this.ws.send(JSON.stringify({
  //     'message': this.message
  //   }));
  // }
}

</script>

<style scoped>

</style>
