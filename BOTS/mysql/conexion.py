import mysql.connector
from config import *

conexion = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, port=PORT, database=DATABASE)
