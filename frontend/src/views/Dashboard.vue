<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useApi } from '../composables/useApi';
import type { MedicionCorporal } from '../app/schemas/medicion'; 

const axios = useApi();
const router = useRouter();
const mediciones = ref<MedicionCorporal[]>([]); // Usamos el tipo para la reactividad

const obtenerMediciones = async () => {
    try {
        const response = await axios.get('/mediciones/');
        mediciones.value = response.data;
        console.log('Mediciones cargadas:', mediciones.value);
    } catch (error) {
        console.error('Error al cargar las mediciones:', error);
    }
};

const irAFormulario = () => {
    router.push('/mediciones/nueva'); // Navega a la nueva ruta del formulario
};

onMounted(() => {
    obtenerMediciones();
});
</script>

<template>
  <div>
    <h1>Tu Historial de Mediciones</h1>
    <button @click="irAFormulario" class="btn btn-primary my-4">
      Añadir Nueva Medición
    </button>
    <hr />
    <div v-if="mediciones.length">
      <div v-for="medicion in mediciones" :key="medicion.id" class="card my-3">
        <div class="card-body">
          <h5 class="card-title">Fecha: {{ medicion.fecha }}</h5>
          <p class="card-text">Peso: {{ medicion.peso }} kg</p>
          <p class="card-text">Altura: {{ medicion.altura }} cm</p>
          <p class="card-text">IMC: {{ medicion.imc }}</p>

          <h6 class="card-subtitle mt-3 mb-2 text-muted">Perímetros (cm)</h6>
          <ul class="list-unstyled">
            <li>Cuello: {{ medicion.cuello }}</li>
            <li>Hombros: {{ medicion.hombros }}</li>
            <li>Pecho: {{ medicion.pecho }}</li>
            <li>Cintura: {{ medicion.cintura }}</li>
            <li>Cadera: {{ medicion.cadera }}</li>
            <li>Brazo Derecho Relajado: {{ medicion.brazo_der_relajado }}</li>
            <li>Brazo Izquierdo Relajado: {{ medicion.brazo_izq_relajado }}</li>
            <li>Brazo Derecho Flexionado: {{ medicion.brazo_der_flexionado }}</li>
            <li>Brazo Izquierdo Flexionado: {{ medicion.brazo_izq_flexionado }}</li>
            <li>Antebrazo Derecho: {{ medicion.antebrazo_der }}</li>
            <li>Antebrazo Izquierdo: {{ medicion.antebrazo_izq }}</li>
            <li>Muslo Derecho: {{ medicion.muslo_der }}</li>
            <li>Muslo Izquierdo: {{ medicion.muslo_izq }}</li>
            <li>Pantorrilla Derecha: {{ medicion.pantorrilla_der }}</li>
            <li>Pantorrilla Izquierda: {{ medicion.pantorrilla_izq }}</li>
          </ul>

          <h6 class="card-subtitle mt-3 mb-2 text-muted">Pliegues Cutáneos (mm)</h6>
          <ul class="list-unstyled">
            <li>Bicipital Derecho: {{ medicion.pliegue_bicipital_der }}</li>
            <li>Bicipital Izquierdo: {{ medicion.pliegue_bicipital_izq }}</li>
            <li>Tricipital Derecho: {{ medicion.pliegue_tricipital_der }}</li>
            <li>Tricipital Izquierdo: {{ medicion.pliegue_tricipital_izq }}</li>
            <li>Subescapular: {{ medicion.pliegue_subescapular }}</li>
            <li>Suprailíaco: {{ medicion.pliegue_suprailiaco }}</li>
            <li>Abdominal: {{ medicion.pliegue_abdominal }}</li>
            <li>Muslo Derecho: {{ medicion.pliegue_muslo_der }}</li>
            <li>Muslo Izquierdo: {{ medicion.pliegue_muslo_izq }}</li>
            <li>Pantorrilla Derecha: {{ medicion.pliegue_pantorrilla_der }}</li>
            <li>Pantorrilla Izquierda: {{ medicion.pliegue_pantorrilla_izq }}</li>
          </ul>
          
          <div v-if="medicion.notas">
            <h6 class="card-subtitle mt-3 mb-2 text-muted">Notas</h6>
            <p class="card-text">{{ medicion.notas }}</p>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <p>No tienes mediciones registradas. ¡Empieza a registrar una!</p>
    </div>
  </div>
  
</template>