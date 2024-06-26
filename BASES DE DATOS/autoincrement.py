import sqlite3

conexion = sqlite3.connect('productos.db')
cursor = conexion.cursor()

cursor.execute('CREATE TABLE productos (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(20), SECCION VARCHAR(20))')

productos = [
    ('Leche', 'Lacteo'),
    ('Pan','Panaderia'),
    ('Gaseosa', 'Bebidas')
]

cursor.executemany("INSERT INTO productos VALUES (NULL,?,?)", productos)
conexion.commit()
conexion.close()