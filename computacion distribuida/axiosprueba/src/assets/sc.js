import { onMounted, onUnmounted, ref } from 'vue';
import axiosInstance from '/src/assets/axios.js';

export function usarJavaScript() {
  const items = ref([]);

  const sec_formulario = ref('');
  const desc_formulario = ref('');
  const path_formulario = ref('');
  const seccion_activa = ref('Inicio');
  const contador_clicks = ref(0);
  let i = 4;

  const openSidebar = () => {
    document.getElementById("sidebar").style.width = "300px";
    console.log('seccion activa de momento', seccion_activa.value)
    document.getElementById(seccion_activa.value).style.marginLeft = "300px";
    document.getElementById("nuestra trayectoria").style.opacity = "0.0";
  };

  const closeSidebar = () => {
    document.getElementById("sidebar").style.width = "0";
    console.log('seccion de cerrar', seccion_activa.value)
    document.getElementById(seccion_activa.value).style.marginLeft = "0";
    document.getElementById("nuestra trayectoria").style.opacity = "100.0";
  };

  const seccionesSidebar = (seccion) => {
    console.log('valores del get', seccion)
    seccion_activa.value = seccion;
    sec_formulario.value = '';
  };

  const crearSeccion = () => {
    i++;
    const nombre = sec_formulario.value;
    const descripcion = desc_formulario.value;
    const path = path_formulario.value;
    items.value = items.value.filter(item => item.name !== nombre);
    items.value.push({
      id: i,
      name: nombre,
      desc: descripcion,
      fotopath: path
    });
    sec_formulario.value = "";
    desc_formulario.value = "";
    path_formulario.value = "";
  };

  const quitarSeccion = (nombre) => {
    items.value = items.value.filter(item => item.name !== nombre);
    sec_formulario.value = "";
  };

  const incrementar = () => { contador_clicks.value++; };

  onMounted(() => {
    document.addEventListener('click', incrementar);
    axiosInstance.post('/regenerar_bd')
      .then(response => {
        console.log('regeneracion', response)
      })
      .catch(error => {
        console.error("Hubo un error en la solicitud de regeneracion: ", error);
      });


      axiosInstance.get('/coger_proyectos')
      .then(response => {
        items.value = response.data;
        console.log('cogida', items.value)
      })
      .catch(error => {
        console.error("Hubo un error en la solicitud de cogida: ", error);
      });

  });

  onUnmounted(() => {
    document.removeEventListener('click', incrementar);
  });

  return {
    items,
    sec_formulario,
    desc_formulario,
    path_formulario,
    i,
    contador_clicks,
    seccion_activa,
    openSidebar,
    closeSidebar,
    seccionesSidebar,
    crearSeccion,
    quitarSeccion
  };
}