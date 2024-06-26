import mysql.connector
from config import *
from funciones import *
conexion = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, port=PORT, database=DATABASE)
cursor = conexion.cursor()


query = f'UPDATE users SET rank = ty WHERE id = 6'

cursor.execute(query)
conexion.commti()