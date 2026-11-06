"""Reto 7 - Mostrar los coches de MySQL en una tabla con PrettyTable."""
from prettytable import PrettyTable

from leerBd import cargar_config, conectar


def tabla_coches():
    conexion = conectar(cargar_config())
    if conexion is None:
        return
    cursor = conexion.cursor()
    cursor.execute("SELECT id, marca, modelo, color, km, precio FROM coches")
    res = cursor.fetchall()

    tabla = PrettyTable(["ID", "Marca", "Modelo", "Color", "Kilometraje", "Precio"])
    for fila in res:
        tabla.add_row(fila)
    tabla.align["Marca"] = "l"
    tabla.align["Modelo"] = "l"
    tabla.align["Kilometraje"] = "r"
    tabla.align["Precio"] = "r"

    print(tabla)
    print(f"Total: {len(res)} coches")
    cursor.close()
    conexion.close()


if __name__ == "__main__":
    tabla_coches()
