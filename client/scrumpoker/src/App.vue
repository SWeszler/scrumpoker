<template>
  <div class="bg-white dark:bg-gray-800">
    <Room/>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import Room from './components/Room.vue';
import './assets/main.css';

@Options({
  components: {
    Room,
  },
})
export default class App extends Vue {}
</script>

<style>

</style>
