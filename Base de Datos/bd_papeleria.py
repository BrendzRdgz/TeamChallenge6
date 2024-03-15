import sqlite3

# Conexión a la base de datos (creará una nueva si no existe)
conexion = sqlite3.connect('papeleria.db')
cursor = conexion.cursor()

# Crear tablas
cursor.execute('''
CREATE TABLE Proveedor (
    Codigo_Proveedor INTEGER PRIMARY KEY,
    Nombre TEXT,
    Direccion TEXT,
    Ciudad TEXT,
    Provincia TEXT
)
''')

cursor.execute('''
CREATE TABLE Categoria (
    Codigo_Categoria INTEGER PRIMARY KEY,
    Nombre TEXT
)
''')

cursor.execute('''
CREATE TABLE Producto (
    Codigo_Producto INTEGER PRIMARY KEY,
    Nombre TEXT,
    Color TEXT,
    Precio REAL,
    Codigo_Categoria INTEGER,
    FOREIGN KEY (Codigo_Categoria) REFERENCES Categoria(Codigo_Categoria)
)
''')

cursor.execute('''
CREATE TABLE Suministro (
    Codigo_Suministro INTEGER PRIMARY KEY,
    Codigo_Proveedor INTEGER,
    Codigo_Producto INTEGER,
    Fecha DATE,
    Cantidad INTEGER,
    FOREIGN KEY (Codigo_Proveedor) REFERENCES Proveedor(Codigo_Proveedor),
    FOREIGN KEY (Codigo_Producto) REFERENCES Producto(Codigo_Producto)
)
''')

# Insertar datos de ejemplo
proveedores = [
    (1, 'Papelería El Lápiz Azul', 'Calle Principal 123', 'Ciudad A', 'Provincia X'),
    (2, 'Papelería La Pluma Dorada', 'Avenida Central 456', 'Ciudad B', 'Provincia Y'),
    (3, 'Papelería El Borrador Mágico', 'Plaza Mayor 789', 'Ciudad C', 'Provincia Z')
]

cursor.executemany('''
INSERT INTO Proveedor (Codigo_Proveedor, Nombre, Direccion, Ciudad, Provincia)
VALUES (?, ?, ?, ?, ?)
''', proveedores)

categorias = [
    (1, 'Cuadernos'),
    (2, 'Bolígrafos'),
    (3, 'Papeles'),
    (4, 'Gomas de borrar'),
    (5, 'Cintas adhesivas')
]

cursor.executemany('''
INSERT INTO Categoria (Codigo_Categoria, Nombre)
VALUES (?, ?)
''', categorias)

productos = [
    (1, 'Cuaderno Rayado', 'Azul', 5.50, 1),
    (2, 'Bolígrafo Azul', 'Azul', 1.25, 2),
    (3, 'Papel Bond A4', 'Blanco', 3.00, 3),
    (4, 'Goma de borrar blanca', 'Blanco', 0.75, 4),
    (5, 'Cinta adhesiva transparente', 'Transparente', 1.50, 5)
]

cursor.executemany('''
INSERT INTO Producto (Codigo_Producto, Nombre, Color, Precio, Codigo_Categoria)
VALUES (?, ?, ?, ?, ?)
''', productos)

suministros = [
    (1, 1, 1, '2024-03-15', 50),
    (2, 2, 2, '2024-03-16', 100),
    (3, 3, 3, '2024-03-17', 200),
    (4, 1, 4, '2024-03-18', 150),
    (5, 2, 5, '2024-03-19', 75)
]

cursor.executemany('''
INSERT INTO Suministro (Codigo_Suministro, Codigo_Proveedor, Codigo_Producto, Fecha, Cantidad)
VALUES (?, ?, ?, ?, ?)
''', suministros)

# Guardar cambios y cerrar conexión
conexion.commit()
conexion.close()

print("Base de datos de papelería creada y datos insertados correctamente.")
