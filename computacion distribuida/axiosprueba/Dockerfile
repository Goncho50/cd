# Etapa 1: Construcción del frontend
FROM node:16 as build-stage

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar solo los archivos de dependencias para aprovechar el caché
COPY package*.json ./

# Instalar dependencias
RUN npm install

# Copiar el resto del código al contenedor
COPY . .

# Construir la aplicación Vue.js
RUN npm run build

# Etapa 2: Configuración de Nginx para servir los archivos estáticos
FROM nginx:alpine as production-stage

# Copiar los archivos estáticos generados por el frontend
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Copiar la configuración personalizada de Nginx
COPY nginx.conf ./

# Exponer el puerto que usará el servidor
EXPOSE 7050

# Comando para ejecutar Nginx
CMD ["nginx", "-g", "daemon off;"]