<template>
  <div>
    <Players msg="Players"/>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import Players from './components/Players.vue';

@Options({
  components: {
    Players,
  },
})
export default class App extends Vue {}
</script>

<style>

</style>
