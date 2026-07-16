import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || null, // Cargar token desde el almacenamiento local
    isAuthenticated: !!localStorage.getItem('token'), // Verificar si hay un token
  }),
  actions: {
    login(token: string) {
      this.token = token;
      this.isAuthenticated = true;
      localStorage.setItem('token', token); // Guardar el token en el almacenamiento local
      // Aquí puedes agregar la lógica para redirigir al usuario
    },
    logout() {
      this.token = null;
      this.isAuthenticated = false;
      localStorage.removeItem('token'); // Eliminar el token
      // Aquí puedes agregar la lógica para redirigir al usuario al login
    }
  }
});