# Reto final: imagen personalizada de MongoDB con la colección de coches precargada.
# Los scripts de /docker-entrypoint-initdb.d se ejecutan la primera vez que arranca
# el contenedor (con la base de datos vacía), así que cualquier máquina que descargue
# la imagen tendrá ya la base de datos "concesionario" con sus 25 coches.
# El usuario y la contraseña NO van en la imagen: se pasan con -e al hacer docker run.
FROM mongo:latest
LABEL maintainer="fantasmadsd" description="MongoDB con la base de datos concesionario (Juego de retos ASIR)"
COPY coches.js /docker-entrypoint-initdb.d/01-coches.js
EXPOSE 27017
