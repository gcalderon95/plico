<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useApi } from '@/composables/useApi' // Usa tu composable
import { useAuthStore } from '@/stores/auth' // Usa la tienda de Pinia

const email = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()
const authStore = useAuthStore()
const apiClient = useApi() // Inicializa la instancia de axios con el interceptor

async function loginUser() {
  try {
    error.value = ''
    
    // Envía la petición usando la instancia de axios de tu composable
    const response = await apiClient.post('http://localhost:8000/login', {
      email: email.value,
      password: password.value
    })
    
    // Almacena el token usando la acción de la tienda de Pinia
    authStore.login(response.data.access_token)

    console.log('Login exitoso. Token guardado:', response.data.access_token)
    router.push('/dashboard')
  } catch (err) {
    error.value = err.response?.data?.detail || 'Error en login'
  }
}
</script>

<template>
  <form
    @submit.prevent="loginUser"
    class="flex flex-col space-y-4 bg-gray-50 p-6 rounded shadow"
  >
    <h2 class="text-xl font-bold text-center">Iniciar sesión</h2>
    <input
      v-model="email"
      type="email"
      placeholder="Email"
      required
      class="border p-2 rounded"
    />
    <input
      v-model="password"
      type="password"
      placeholder="Contraseña"
      required
      class="border p-2 rounded"
    />
    <button
      type="submit"
      class="bg-blue-600 text-white py-2 rounded hover:bg-blue-700"
    >
      Entrar
    </button>
    <p v-if="error" class="text-red-500 text-sm text-center">{{ error }}</p>
  </form>
</template>