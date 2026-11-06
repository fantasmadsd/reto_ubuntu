# reto_ubuntu

Repositorio del **Juego de retos de Docker** (2.º ASIR, Servicios de Red e Internet).

Esta carpeta (`C:\volumenes\reto_ubuntu`) está montada como *bind mount* en el contenedor
`reto_ubuntu_python`, en la ruta `/home/ubuntu/python`. Así los scripts se editan en Windows
y se ejecutan dentro del contenedor Ubuntu.

## Contenido

| Archivo | Reto | Descripción |
|---|---|---|
| `prueba.txt` | 2 | Archivo creado dentro del contenedor que aparece en el host |
| `sql/coches.sql` | 4 | Crea la base de datos `bdcoches` y la tabla `coches` con 25 registros |
| `leerBd.py` | 5 y 6 | Lee los coches de MySQL; la conexión se toma de `config.json` |
| `tablaCoches.py` | 7 | Muestra los coches de MySQL en una tabla con PrettyTable |
| `mongo/coches.js` | 8 | Crea la base de datos `concesionario` e inserta los coches en MongoDB |
| `mongo/consultas.js` | 8 | Consultas de comprobación (`find().pretty()`, recuento, etc.) |
| `leerMongo.py` | 9 | Lee la colección `coches` con pymongo y la muestra en tabla |
| `config.example.json` | 6 | Plantilla de configuración **sin credenciales** |
| `.gitignore` | 6 | Excluye `config.json`, `.env` y `__pycache__` |

## Contenedores

| Contenedor | Imagen | Red | Puertos |
|---|---|---|---|
| `reto_ubuntu_python` | `imagen-reto-ubuntu` (personalizada, reto 1) | `red_retos` | — |
| `reto_mysql` | `mysql:latest` | `red_retos` | 3308 → 3306 |
| `reto_mongo` | `mongo:latest` | `red_retos` | 27017 → 27017 |

Los contenedores comparten la red `red_retos`, así que los scripts se conectan usando el nombre
del contenedor (`reto_mysql`, `reto_mongo`) en lugar de una IP que puede cambiar.

## Uso

```bash
# 1. Crear la configuración local (no se sube a Git)
cp config.example.json config.json   # y rellenar las contraseñas

# 2. Ejecutar los scripts dentro del contenedor
docker exec -w /home/ubuntu/python reto_ubuntu_python python3 leerBd.py
docker exec -w /home/ubuntu/python reto_ubuntu_python python3 tablaCoches.py
docker exec -w /home/ubuntu/python reto_ubuntu_python python3 leerMongo.py
```

Dependencias en el contenedor: `python3`, `python3-mysql.connector`, `python3-prettytable`
y `python3-pymongo`.
