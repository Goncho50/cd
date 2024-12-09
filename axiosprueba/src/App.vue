<template>
  <body class="body" >
   <div id="sidebar" class="sidebar">
    <a href="#" class="boton-cerrar" @click="closeSidebar">&times;</a>
    <ul class="menu">
     <a href="#" @click="seccionesSidebar('Inicio')">Inicio</a>
     <li v-for="elem in items" :key="elem.id">
       <a href="#" @click="seccionesSidebar(elem.name)">{{elem.name}}</a>
     </li>
     <br> <br>

     <a href="#" @click="seccionesSidebar('formulario')">Crear sección</a>
     <a href="#" @click="seccionesSidebar('quitar_seccion')">Quitar sección</a>
     <br> <a>contador de clicks: <br> {{ contador_clicks }}</a>
    </ul>
   </div>

   <div class="seccion" id="Inicio" v-if="seccion_activa === 'Inicio'">
    <p class="title-box" id="title-box"><b>PORTFOLIO COMPUTACIÓN DISTRIBUIDA</b></p>
    <img class="fotos" src="./assets/david.png">
    <img class="fotos" src="./assets/goncho.png">
    <div class="texto">
      <div class= "section"><b>¿QUIENES SOMOS?</b><br>Somos estudiantes del tercer año de <br>Ciencia e Ingeniería de Datos en la UAM.</div>

      <div class= "section"><b> NUESTROS PROYECTOS</b><br>A lo largo de tres años hemos realizado diversas prácticas <br>orientadas a distintos ámbitos relacionados con la ciencia de datos, como análisis algoritmos, estructuras de datos, programación dinámica y funcional, manejo de bases de datos...</div>

      <div class= "section"><b> SABER MÁS...</b><br>Pinchando en el botón de abajo podréis indagar sobre los trabajos <br>que hemos desarrollado durante este tiempo.</div>
    </div>

    <div> <br> <br>Buscador de proyectos:
      <input v-model="sec_formulario" @keyup.enter="seccionesSidebar(sec_formulario)" placeholder="Escribe aquí">
    </div>
     <br> <br> <i @click="openSidebar" id="nuestra trayectoria" class="menu-icon">Nuestra trayectoria</i>

   </div>



   <div class="seccion" v-if="seccion_activa === 'formulario'">
     <h1 class="contenedor">CREAR SECCIÓN</h1>
     <br>
     <div class="textohs">
       <div>Nombre del nuevo proyecto: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<input v-model="sec_formulario" placeholder="Escribe aquí"></div>
       <br>
       <div>Descripción del nuevo proyecto:  &nbsp; &nbsp; &nbsp;<input v-model="desc_formulario" placeholder="Escribe aquí"></div>
       <br>
       <div>Ruta de imagen: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
       <input v-model="path_formulario" placeholder="Escribe aquí">
       <br><br>NOTA: Si no quieres incluir ninguna imagen, deja este campo libre.<br>Además, la imagen debe estar contenida en la carpeta del proyecto.
       <br></div>

       <br>

       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<button @click="crearSeccion">Agregar nuevo proyecto</button>
     </div>
     <i id="nuestra trayectoria" class="menu-icon" @click="openSidebar">Ver más &equiv;</i>
   </div>


   <div class="seccion" v-if="seccion_activa === 'quitar_seccion'">
     <h1 class="contenedor">QUITAR SECCIÓN</h1>
     <br><br>
     <div class="textohs">


      <div>
       Introduce debajo el nombre del que deseas eliminar.<br>
       No podrás borrar las secciones de Inicio, Crear Sección y Quitar Sección.
       <br><br>
       &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;
       <input placeholder="Escribe aquí" v-model="sec_formulario">&nbsp;&nbsp;&nbsp;
       <button @click="quitarSeccion(sec_formulario)">Quitar proyecto</button>
     </div>

     </div>
     <i id="nuestra trayectoria" class="menu-icon" @click="openSidebar">Ver más &equiv;</i>
   </div>

   <ul>
     <li v-for="elem in items" :key="elem.id">
       <div class="seccion" :id="elem.name" v-if="seccion_activa === elem.name">
        <div >
         <h1 class="contenedor">{{ elem.name }}</h1>
        </div>
         <div>
           <p class="textohs">{{ elem.desc }}</p>
         </div>
         <i id="nuestra trayectoria" class="menu-icon" @click="openSidebar">Ver más &equiv;</i>
         <img v-if="elem.fotopath !==''" class="fotos_secciones" :src="elem.fotopath"> <!--El prefijo : es la abreviatura de v-bind. Esto le dice a Vue.js que debe enlazar dinámicamente el valor de elem.fotopath al atributo src del elemento <img>. -->
        </div>
     </li>
     <br>
   </ul>
 </body>
 </template>

 <script>
 import '/src/assets/ejercicio2.css';
 import { usarJavaScript } from '/src/assets/sc.js'; // Importa la lógica desde el archivo externo

export default {
  setup() {
    const {
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
    } = usarJavaScript();  // Usa la función para importar toda la lógica

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
};
</script>