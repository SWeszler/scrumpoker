<template>
  <div>
    <div class="flex justify-between mb-10">
      <router-link to="/">ScrumPoker</router-link>
      <div v-if="$store.state.isAuthenticated">
        <a>Logout</a>
      </div>
      <div v-else>
        <router-link to="/login">Login</router-link>
      </div>
    </div>
    <router-view />
  </div>
</template>
