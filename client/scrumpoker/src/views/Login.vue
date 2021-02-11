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
        <button @click="login" class="mr-5 bg-blue-400 hover:bg-blue-dark text-white font-bold py-2 px-4 rounded" type="button">
          Login In
        </button>
        <button @click="signup" class="bg-green-400 hover:bg-blue-dark text-white font-bold py-2 px-4 rounded" type="button">
          Sign Up
        </button>
      </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, getCurrentInstance } from 'vue';
import { useStore } from 'vuex';

export default defineComponent({
  setup(_, ctx){
    const username = ref('');
    const password = ref('');
    const store = useStore();
    const { ...context } = getCurrentInstance() as NonNullable<ReturnType<typeof getCurrentInstance>>;
    
    async function login(){
      const data = {
        username: username.value,
        password: password.value
      };

      const response = await context.appContext.app.axios.post('api/token/', data);

      localStorage.setItem('access_token', response.data.access);
      localStorage.setItem('refresh_token', response.data.refresh);


    }

    return { username, password, login }
  }

});
</script>

