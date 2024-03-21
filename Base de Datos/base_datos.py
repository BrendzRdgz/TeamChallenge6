import sqlite3
from pathlib import Path

# Especifica la ubicación y el nombre del archivo de la base de datos
nombre_base_de_datos = "basedatos.db"
ruta_carpeta = Path("Base de Datos")  # Solo especifica el nombre de la carpeta, no la base de datos

# Convierte la ruta en una cadena
ruta_base_de_datos = str(ruta_carpeta / nombre_base_de_datos)

# Conecta con la base de datos (si no existe, se creará automáticamente)
conexion = sqlite3.connect(ruta_base_de_datos)
conexion.close()

print(f"Se ha creado la base de datos en {ruta_base_de_datos}")
    