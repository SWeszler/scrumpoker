import { createStore } from "vuex";
import axios from "@/axios";

export default createStore({
  state: {
    accessToken: localStorage.getItem("access_token") || "",
    refreshToken: localStorage.getItem("refresh_token") || "",
    isAuthenticated: false
  },
  mutations: {
    SAVE_AUTH(state, data) {
      state.accessToken = data.access;
      state.accessToken = data.refresh;
      localStorage.setItem("access_token", data.access);
      localStorage.setItem("refresh_token", data.refresh);
      state.isAuthenticated = true;
    }
  },
  actions: {
    async refreshToken({ commit, state }) {
      try {
        const response = await axios.post("api/token/refresh/", {
          refresh: state.refreshToken
        });
        response.data.refresh = state.refreshToken;
        commit("SAVE_AUTH", response.data);
      } catch (err) {
        console.error(err);
      }
    }
  },
  modules: {}
});
