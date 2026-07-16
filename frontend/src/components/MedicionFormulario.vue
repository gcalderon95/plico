<template>
  <form @submit.prevent="guardarMedicion" class="space-y-2">
    <input v-model="form.fecha" type="date" required />

    <h2> Datos generales</h2>
    <input v-model.number="form.peso" type="number" step="0.01" placeholder="Peso (kg)" />
    <input v-model.number="form.altura" type="number" step="0.01" placeholder="Altura (cm)" />
    <input v-model.number="form.imc" type="number" step="0.01" placeholder="IMC" />

    <h2>Perimetros</h2>
    <input v-model.number="form.cuello" type="number" step="0.01" placeholder="Cuello (cm)" />
    <input v-model.number="form.hombros" type="number" step="0.01" placeholder="Hombros (cm)" />
    <input v-model.number="form.pecho" type="number" step="0.01" placeholder="Pecho (cm)" />
    <input v-model.number="form.cintura" type="number" step="0.01" placeholder="Cintura (cm)" />
    <input v-model.number="form.cadera" type="number" step="0.01" placeholder="Cadera (cm)" />
    <input v-model.number="form.brazo_der_relajado" type="number" step="0.01" placeholder="Brazo derecho relajado (cm)" />
    <input v-model.number="form.brazo_izq_relajado" type="number" step="0.01" placeholder="Brazo izquierdo relajado (cm)" />
    <input v-model.number="form.brazo_der_flexionado" type="number" step="0.01" placeholder="Brazo derecho flexionado (cm)" />
    <input v-model.number="form.brazo_izq_flexionado" type="number" step="0.01" placeholder="Brazo izquierdo flexionado (cm)" />
    <input v-model.number="form.antebrazo_der" type="number" step="0.01" placeholder="Antebrazo derecho (cm)" />
    <input v-model.number="form.antebrazo_izq" type="number" step="0.01" placeholder="Antebrazo izquierdo (cm)" />
    <input v-model.number="form.muslo_der" type="number" step="0.01" placeholder="Muslo derecho (cm)" />
    <input v-model.number="form.muslo_izq" type="number" step="0.01" placeholder="Muslo izquierdo (cm)" />
    <input v-model.number="form.pantorrilla_der" type="number" step="0.01" placeholder="Pantorrilla derecha (cm)" />
    <input v-model.number="form.pantorrilla_izq" type="number" step="0.01" placeholder="Pantorrilla izquierda (cm)" />

    <h2>Pliegues cutaneos</h2>
    <input v-model.number="form.pliegue_bicipital_der" type="number" step="0.01" placeholder="Pliegue bicipital derecho (mm)" />
    <input v-model.number="form.pliegue_bicipital_izq" type="number" step="0.01" placeholder="Pliegue bicipital izquierdo (mm)" />
    <input v-model.number="form.pliegue_tricipital_der" type="number" step="0.01" placeholder="Pliegue tricipital derecho (mm)" />
    <input v-model.number="form.pliegue_tricipital_izq" type="number" step="0.01" placeholder="Pliegue tricipital izquierdo (mm)" />
    <input v-model.number="form.pliegue_subescapular" type="number" step="0.01" placeholder="Pliegue subescapular (mm)" />
    <input v-model.number="form.pliegue_suprailiaco" type="number" step="0.01" placeholder="Pliegue suprailiaco (mm)" />
    <input v-model.number="form.pliegue_abdominal" type="number" step="0.01" placeholder="Pliegue abdominal (mm)" />
    <input v-model.number="form.pliegue_muslo_der" type="number" step="0.01" placeholder="Pliegue muslo derecho (mm)" />
    <input v-model.number="form.pliegue_muslo_izq" type="number" step="0.01" placeholder="Pliegue muslo izquierdo (mm)" />
    <input v-model.number="form.pliegue_pantorrilla_der" type="number" step="0.01" placeholder="Pliegue pantorrilla derecha (mm)" />
    <input v-model.number="form.pliegue_pantorrilla_izq" type="number" step="0.01" placeholder="Pliegue pantorrilla izquierda (mm)" />

    <h3>Notas</h3>
    <textarea v-model="form.notas" placeholder="Notas adicionales"></textarea>

    <button type="submit">Guardar</button>
  </form>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useApi } from '../composables/useApi'; // Asegúrate de que la ruta sea correcta

// Obtén la instancia de Axios a través del composable
const axios = useApi();

const hoy = new Date().toISOString().slice(0, 10);

const form = ref({
  fecha: hoy,
  peso: null,
  altura: null,
  imc: null,
  cuello: null,
  hombros: null,
  pecho: null,
  cintura: null,
  cadera: null,
  brazo_der_relajado: null,
  brazo_izq_relajado: null,
  brazo_der_flexionado: null,
  brazo_izq_flexionado: null,
  antebrazo_der: null,
  antebrazo_izq: null,
  muslo_der: null,
  muslo_izq: null,
  pantorrilla_der: null,
  pantorrilla_izq: null,
  pliegue_bicipital_der: null,
  pliegue_bicipital_izq: null,
  pliegue_tricipital_der: null,
  pliegue_tricipital_izq: null,
  pliegue_subescapular: null,
  pliegue_suprailiaco: null,
  pliegue_abdominal: null,
  pliegue_muslo_der: null,
  pliegue_muslo_izq: null,
  pliegue_pantorrilla_der: null,
  pliegue_pantorrilla_izq: null,
  notas: ''
});

const guardarMedicion = async () => {
  try {
    console.log(JSON.stringify(form.value, null, 2));
    await axios.post('/mediciones/', form.value); 
    alert('Guardado correctamente');
  } catch (err) {
    console.error(err);
    alert('Error al guardar');
  }
};
</script>