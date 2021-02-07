<template>
  <div>
    <h1 class="bg-sw-logo bg-no-repeat bg-center pb-10 pt-5 text-4xl text-center font-bold text-white antialiased opacity-70">ScrumPoker</h1>
    <div v-if="logged">
      <Room/>
    </div>
    <div v-else class="container mx-auto flex justify-center items-center">
      <Login/>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import Room from './components/Room.vue';
import Login from './components/Login.vue';
import './assets/main.css';

export default defineComponent({
  components: {
    Room,
    Login
  },
  setup(){
    const logged = ref(false);

    return { logged };
  }
});
</script>

<style>

</style>
