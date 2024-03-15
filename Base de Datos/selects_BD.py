import sqlite3
import pandas as pd

# Conexión a la base de datos (creará una nueva si no existe)
conexion = sqlite3.connect('papeleria.db')
cursor = conexion.cursor()

def sql_query(query):
    cursor.execute(query)
    datos = cursor.fetchall()
    col = [description[0] for description in cursor.description]
    return pd.DataFrame(datos,columns=col)

query = '''
SELECT *
FROM Proveedor
'''
#sql_query(query)


cursor.execute(query)
resultado = cursor.fetchall()
df = pd.DataFrame(resultado)
df