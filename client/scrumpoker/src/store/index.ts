import { createStore } from "vuex";

export default createStore({
  state: {
    accessToken: null as string | null,
    refreshToken: null as string | null
  },
  mutations: {
    INITIALIZE_STORE(state){
      state.accessToken = localStorage.getItem('access_token');
      state.refreshToken = localStorage.getItem('refresh_token');
    }
  },
  actions: {},
  modules: {}
});
