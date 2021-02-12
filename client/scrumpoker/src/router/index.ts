import store from "@/store";
import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Home from "../views/Home.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: {
      requiresAuth: false
    }
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("../views/Login.vue"),
    meta: {
      requiresAuth: false
    }
  },
  {
    path: "/room",
    name: "Room",
    component: () => import("../views/Room.vue"),
    meta: {
      requiresAuth: true
    }
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

router.beforeEach((to, from, next) => {
  if (to.name === "Login") {
    store.dispatch("refreshToken").then(() => {
      if (store.state.isAuthenticated) {
        next({ name: "Room" });
      } else {
        next();
      }
    });
  } else if (!to.meta.requiresAuth || store.state.isAuthenticated) {
    next();
  } else {
    store.dispatch("refreshToken").then(() => {
      if (store.state.isAuthenticated) {
        next();
      } else {
        next({ name: "Login" });
      }
    });
  }
});

export default router;
