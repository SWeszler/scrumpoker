<template>
  <div>
    <div class="flex justify-between">
      <router-link to="/">Home</router-link>
      <div v-if="$store.state.user">
        <span v-text="$store.state.user"></span>
      </div>
      <div v-else>
        <router-link to="/login">Login/Signup</router-link>
      </div>
    </div>
    <router-view />
  </div>
</template>
