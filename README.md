# project_yugioh
Proyecto de Computer Vision. Detectar tipos de cartas del juego Yu-Gi-Oh.

# installer dependencias en ambiente virtual
pip install -r requirements.txt

# crear una red privada para contenedores docker
docker network create shared_network

# levantar el proyecto
$ docker-compose up --build -d