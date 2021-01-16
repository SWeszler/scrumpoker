<template>
  <div>
    <h1 class=" text-xl text-center font-bold">Welcome to Scrumpoker!</h1>
    <div v-if="isLogged">
      <Room/>
    </div>
    <div v-else>
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
