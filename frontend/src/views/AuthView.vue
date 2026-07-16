<template>
  <div>
    <button @click="tab = 'login'">Login</button>
    <button @click="tab = 'registro'">Registro</button>

    <Login v-if="tab === 'login'" />
    <Registro v-else />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import Login from '../components/Login.vue'
import Registro from '../components/Registro.vue'

const tab = ref('login')
</script>
