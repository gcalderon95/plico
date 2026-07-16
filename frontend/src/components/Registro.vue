<template>
  <form
    @submit.prevent="handleRegister"
    class="flex flex-col space-y-4 bg-gray-50 p-6 rounded shadow"
  >
    <h2 class="text-xl font-bold text-center">Registro</h2>
    <input
      v-model="nombre"
      placeholder="Nombre"
      required
      class="border p-2 rounded"
    />
    <input
      v-model="email"
      type="email"
      placeholder="Correo"
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
      class="bg-green-600 text-white py-2 rounded hover:bg-green-700"
    >
      Registrarme
    </button>
    <p v-if="message" class="text-center text-sm text-green-600">{{ message }}</p>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const nombre = ref('')
const email = ref('')
const password = ref('')
const message = ref('')

async function handleRegister() {
  try {
    const response = await axios.post('http://127.0.0.1:8000/registro', {
      nombre: nombre.value,
      email: email.value,
      password: password.value
    })
    message.value = response.data.msg
  } catch (error) {
    message.value = error.response?.data?.detail || 'Error al registrar'
  }
}
</script>
