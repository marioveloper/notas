#importamos nuestra libreria
import sqlite3

#creamos la base de datos
conexion = sqlite3.connect('mibase.db')

#creamos el cursor
cursor = conexion.cursor()

#crear la tabla
cursor.execute('CREATE TABLE IF NOT EXISTS usuarios'\
    '(nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))')

#guardar los cambios
conexion.commit()

#cerramos la conexion
conexion.close()