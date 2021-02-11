<template>
  <div>
    <div class="flex justify-between">
      <router-link to="/">Home</router-link>
      <router-link to="/login">Login/Signup</router-link>
    </div>
    <router-view />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useStore } from 'vuex';

export default defineComponent({
  setup(){
    const store = useStore();
    store.commit('INITIALIZE_STORE');
  }
});
</script>

