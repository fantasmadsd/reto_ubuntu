"""Reto 5 - Leer los coches de la base de datos MySQL desde Python."""
import os

import mysql.connector

# Datos de conexión. El contenedor reto_mysql está en la red Docker red_retos,
# así que se resuelve por su nombre. La contraseña se recibe por variable de
# entorno para no dejarla escrita en el repositorio.
config = {
    "user": "root",
    "password": os.environ.get("DB_PASSWORD", ""),
    "host": "reto_mysql",
    "database": "bdcoches",
}


def conectar(config):
    conexion = mysql.connector.connect(**config)
    if conexion.is_connected():
        print("Conexión establecida a la BD\n")
        return conexion
    print("No se ha podido conectar a la BD")
    return None


def consulta_coches():
    conexion = conectar(config)
    if conexion is None:
        return
    # El cursor gestiona la llamada y el retorno de los datos
    cursor = conexion.cursor()
    cursor.execute("SELECT id, marca, modelo, color, km, precio FROM coches")
    res = cursor.fetchall()
    for id_, marca, modelo, color, km, precio in res:
        print(f"{id_:>2}. {marca} {modelo} ({color}) - {km} km - {precio} €")
    print(f"\nTotal: {len(res)} coches")
    cursor.close()
    conexion.close()


consulta_coches()
