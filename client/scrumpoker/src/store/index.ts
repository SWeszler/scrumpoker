import { createStore } from "vuex";

export default createStore({
  state: {
    accessToken: localStorage.getItem('access_token') || '',
    refreshToken: localStorage.getItem('refresh_token') || '',
    user: '',
  },
  mutations: {
    AUTH_SUCCESS(state, data){
      state.accessToken = data.access;
      state.accessToken = data.refresh;
      state.user = data.user;
      localStorage.setItem('access_token', data.access);
      localStorage.setItem('refresh_token', data.refresh);
    }
  },
  actions: {},
  modules: {}
});
