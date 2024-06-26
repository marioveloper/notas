#importamos nuestra libreria
import sqlite3

#creamos la base de datos
conexion = sqlite3.connect('mibase.db')

#creamos el cursor
cursor = conexion.cursor()

#crear la tabla
#cursor.execute("CREATE TABLE usuarios\
#            (dni VARCHAR(11)PRIMARY KEY,\
#            nombre VARCHAR(100),\
#            edad INTEGER,\
#            email VARCHAR(100))")

cursor.execute('INSERT INTO usuarios VALUES '\
                '("99031812645", "mario", 24, "mario@gmail.com")')


#guardar los cambios
conexion.commit()

#cerramos la conexion
conexion.close()