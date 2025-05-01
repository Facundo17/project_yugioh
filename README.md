# project_yugioh
Proyecto de Computer Vision. Detectar tipos de cartas del juego Yu-Gi-Oh.

# Alcance del proyecto
Este proyecto conciste en seleccionar una carta, enviara a través de un API, y devolver el tipo de carta.
Solamente se clasifican tres tipos de cartas: Monster, Spell, Trap.

# STACK
* HTML/CSS/JAVASCRIPT para la UI.
* FastAPI para la comunicación entre los servicios del modelo
* Tensorflow/Keras como modelo de clasificación.
* Docker para la arquitectura de microservicios

# Instalar dependencias en ambiente virtual
pip install -r requirements.txt

# Crear una red privada para contenedores docker
docker network create shared_network

# levantar el proyecto
docker-compose up --build -d

# ejecutar clasificador
streamlit run classification.py