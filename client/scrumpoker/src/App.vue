<template>
  <div>
    <h1 class="bg-sw-logo bg-no-repeat bg-center pb-10 pt-5 text-4xl text-center font-bold text-white antialiased opacity-70">ScrumPoker</h1>
    <div v-if="isLogged">
      <Room/>
    </div>
    <div v-else class="container mx-auto flex justify-center items-center">
      <Login/>
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import Room from './components/Room.vue';
import Login from './components/Login.vue';
import './assets/main.css';

@Options({
  components: {
    Room,
    Login
  },
})
export default class App extends Vue {
  isLogged: boolean = false;

  created(){

  }

}
</script>

<style>

</style>
