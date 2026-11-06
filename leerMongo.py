"""Reto 9 - Leer la colección coches de MongoDB con pymongo y mostrarla en tabla."""
import json
import sys
from pathlib import Path

from prettytable import PrettyTable
from pymongo import MongoClient
from pymongo.errors import PyMongoError

RUTA_CONFIG = Path(__file__).with_name("config.json")


def cargar_config(ruta=RUTA_CONFIG):
    """Lee los datos de conexión de config.json (excluido del repo por .gitignore)."""
    if not ruta.exists():
        sys.exit(f"No existe {ruta.name}. Copia config.example.json a config.json y rellénalo.")
    with open(ruta, encoding="utf-8") as f:
        return json.load(f)["mongo"]


def conectar(cfg):
    """Conexión estable: timeout corto, comprobación con ping y error claro si falla."""
    uri = (f"mongodb://{cfg['user']}:{cfg['password']}@{cfg['host']}:{cfg['port']}/"
           f"{cfg['database']}?authSource=admin")
    cliente = MongoClient(uri, serverSelectionTimeoutMS=5000)
    try:
        cliente.admin.command("ping")
    except PyMongoError as e:
        sys.exit(f"No se ha podido conectar a MongoDB: {e}")
    print("Conexión establecida a MongoDB")
    print("Bases de datos disponibles:", cliente.list_database_names(), "\n")
    return cliente


def tabla_coches():
    cfg = cargar_config()
    cliente = conectar(cfg)
    try:
        coleccion = cliente[cfg["database"]]["coches"]
        coches = coleccion.find().sort("id", 1)

        tabla = PrettyTable(["_id", "ID", "Marca", "Modelo", "Color", "Kilometraje", "Precio"])
        for coche in coches:
            # .get() evita errores si a algún documento le falta un campo
            tabla.add_row([
                coche.get("_id", ""),
                coche.get("id", ""),
                coche.get("marca", ""),
                coche.get("modelo", ""),
                coche.get("color", ""),
                coche.get("km", ""),
                coche.get("precio", ""),
            ])
        tabla.align["Marca"] = "l"
        tabla.align["Modelo"] = "l"
        print(tabla)
        print(f"Total: {coleccion.count_documents({})} coches")
    finally:
        cliente.close()


if __name__ == "__main__":
    tabla_coches()
