"""Reto 5/6 - Leer los coches de MySQL con la configuración en config.json."""
import json
import sys
from pathlib import Path

import mysql.connector

RUTA_CONFIG = Path(__file__).with_name("config.json")


def cargar_config(ruta=RUTA_CONFIG):
    """Lee los datos de conexión de config.json (excluido del repo por .gitignore)."""
    if not ruta.exists():
        sys.exit(f"No existe {ruta.name}. Copia config.example.json a config.json y rellénalo.")
    with open(ruta, encoding="utf-8") as f:
        return json.load(f)["mysql"]


def conectar(config):
    conexion = mysql.connector.connect(**config)
    if conexion.is_connected():
        print("Conexión establecida a la BD\n")
        return conexion
    print("No se ha podido conectar a la BD")
    return None


def consulta_coches():
    conexion = conectar(cargar_config())
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


if __name__ == "__main__":
    consulta_coches()
