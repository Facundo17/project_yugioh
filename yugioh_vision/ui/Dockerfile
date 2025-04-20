# Dockerfile para ui-service usando Nginx
FROM nginx:alpine

# Elimina el contenido por defecto de Nginx
RUN rm -rf /usr/share/nginx/html/*

# Copia el archivo HTML al directorio de Nginx
COPY main.html /usr/share/nginx/html/index.html

# Exponer el puerto estándar
EXPOSE 80