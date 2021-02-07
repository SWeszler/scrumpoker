import { createApp } from 'vue'
import App from './App.vue'
import config from './config.js'

const app = createApp(App);
app.config.globalProperties.$api = config.API_URL;
app.mount('#app');
