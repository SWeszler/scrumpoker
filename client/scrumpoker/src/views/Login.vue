<template>
  <div class="md:min-w-400 bg-white opacity-70 shadow-md rounded px-8 pt-6 pb-8 mb-4">
      <div class="mb-4">
        <label class="block text-grey-darker text-sm font-bold mb-2" for="username">
          Username
        </label>
        <input v-model="username" class="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker" id="username" type="text" placeholder="Username">
      </div>
      <div class="mb-6">
        <label class="block text-grey-darker text-sm font-bold mb-2" for="password">
          Password
        </label>
        <input v-model="password" class="shadow appearance-none border border-red rounded w-full py-2 px-3 text-grey-darker mb-3" id="password" type="password" placeholder="******************">
      </div>
      <div class="flex">
        <button id="login" @click="login" class="mr-5 bg-blue-400 hover:bg-blue-dark text-white font-bold py-2 px-4 rounded" type="button">
          Login
        </button>
        <button @click="signup" class="bg-green-400 hover:bg-blue-dark text-white font-bold py-2 px-4 rounded" type="button">
          Signup
        </button>
      </div>
      <div>{{error}}</div>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, toRefs } from 'vue';
import { useStore } from 'vuex';
import router from "../router";
import axios from "../axios";

export default defineComponent({
  setup(){
    const compData = reactive({
      username: '',
      password: '',
      error: ''
    });
    const store = useStore();
    
    async function login(){
      const data = {
        username: compData.username,
        password: compData.password
      };
      let success = false;

      try {
        const response = await axios.post('api/token/', data);
        store.commit('SAVE_AUTH', response.data);
        success = true;
      } catch (error) {
        compData.error = error;
      }

      if(success) {
        router.push('/room');
      }
    }

    return { login, ...toRefs(compData) }
  }

});
</script>

