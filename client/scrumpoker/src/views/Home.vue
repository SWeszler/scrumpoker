<template>
  <div class="text-center p-10">
    <img class="inline-block" alt="Scrumpoker Logo" src="../assets/logo.svg" />
    <p>Welcome to Scrumpoker.</p>
    <p v-if="logged">User Name!</p>
    <p v-else>Login to start the game!</p>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  setup() {
    const logged = ref(false);

    return { logged };
  }
});
</script>
