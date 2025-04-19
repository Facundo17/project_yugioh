# Usa una imagen base con Python y TensorFlow
FROM tensorflow/tensorflow:2.12.0

# Instala dependencias del sistema (para opencv)
RUN apt-get update && apt-get install -y \
    ffmpeg libsm6 libxext6 libgl1-mesa-glx \
    && apt-get clean

# Crea y entra en el directorio del proyecto
WORKDIR /app

# Copia tus archivos al contenedor (modelo + script)
COPY . /app

# Instala las dependencias de Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Punto de entrada por defecto
CMD ["python", "ml_service.py"]