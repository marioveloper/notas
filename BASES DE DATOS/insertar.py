#importamos nuestra libreria
import sqlite3

#creamos la base de datos
conexion = sqlite3.connect('mibase.db')

#creamos el cursor
cursor = conexion.cursor()

#insertar datos
cursor.execute('INSERT INTO usuarios VALUES '\
                '("mario", 24, "mario@gmail.com")')


#guardar los cambios
conexion.commit()

#cerramos la conexion
conexion.close()