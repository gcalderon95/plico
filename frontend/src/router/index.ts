import { createRouter, createWebHistory } from 'vue-router'
import AuthView from '../views/AuthView.vue'
import Dashboard from '../views/Dashboard.vue'
import MedicionFormulario from '../components/MedicionFormulario.vue'

const routes = [
  {
    path: '/',
    name: 'Auth',
    component: AuthView,
  },
  {
    path: '/Dashboard',
    name: 'Dashboard',
    component: Dashboard,
  },
  {
      path: '/mediciones/nueva',
      name: 'nueva-medicion',
      component: MedicionFormulario
    },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
