<template>
  <div class="text-center p-10">
    <img
      class="inline-block w-10"
      alt="Scrumpoker Logo"
      src="../assets/logo.svg"
    />
    <p class="mb-10">Welcome to Scrumpoker.</p>
    <div v-if="$store.state.isAuthenticated">
      <router-link
        class="focus:outline-none hover:bg-gray-400 pt-1 pb-1 pr-3 pl-3 shadow-md rounded-full bg-gray-300"
        to="/room"
        >Enter Room</router-link
      >
    </div>
    <div v-else>Login to start the game!</div>
  </div>
</template>
