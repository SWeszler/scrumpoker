import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App);
app.config.globalProperties.$api = 'http://localhost:5000/';
app.mount('#app');
