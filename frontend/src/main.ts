// main.ts
import { createApp } from 'vue';
import { createPinia } from 'pinia'; 
import App from './App.vue';
import router from './router';
import axios from 'axios';


import { useAuthStore } from './stores/auth';


const app = createApp(App);
const pinia = createPinia();

app.use(pinia);


const authStore = useAuthStore();


const apiClient = axios.create({
  baseURL: 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json',
  },
});

apiClient.interceptors.request.use(
  (config) => {
    const token = authStore.token; 
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);


app.config.globalProperties.$axios = apiClient;


app.use(router);
app.mount('#app');