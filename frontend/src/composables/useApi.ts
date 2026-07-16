import { getCurrentInstance } from 'vue';
import type { AxiosInstance } from 'axios';
// Define el tipo para la instancia de Axios global
interface GlobalProperties {
  $axios: AxiosInstance;
}

/**
 * Hook de composición para obtener la instancia de Axios configurada globalmente.
 * Debe ser llamado dentro del setup de un componente.
 */
export function useApi(): AxiosInstance {
  const app = getCurrentInstance();
  
  if (!app) {
    throw new Error('useApi debe ser llamado dentro del setup de un componente.');
  }
  
  // Accede a las propiedades globales y asume el tipo correcto
  const { $axios } = app.appContext.config.globalProperties as GlobalProperties;
  
  if (!$axios) {
    throw new Error('La instancia de Axios no está disponible. ¿La configuraste en main.ts?');
  }

  return $axios;
}