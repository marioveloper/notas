import mysql.connector
from config import *

conexion = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, port=PORT, database=DATABASE)
cursor = conexion.cursor()

def activar_usuario(id):
    #actuvo el usuario
    cursor.execute(f'UPDATE users SET active = 1 WHERE id = "{id}"')
    conexion.commit()



    tabla = cursor.execute(f'SELECT referred_by, status FROM users WHERE id = {id}')
    tabla = cursor.fetchall()
    referred_by = tabla[0][0]
    status = tabla[0][1]

    if status ==0:
        #actualizo el status
        status+=1
        cursor.execute(f'UPDATE users SET status = {status} WHERE id = "{id}"')

        #si se cumple la condicion anade un referido al padre
        if referred_by:
            referrals = cursor.execute(f'SELECT referrals FROM users WHERE telegram_id = {referred_by}')
            referrals = cursor.fetchall()[0][0]
            referrals += 1
            cursor.execute(f'UPDATE users SET referrals = {referrals} WHERE telegram_id = "{referred_by}"')
        conexion.commit()

def desactivar_usuario(id):
    cursor.execute(f'UPDATE users SET active = 0 WHERE id = "{id}"')
    conexion.commit()

def colocar_rango(id):
    pass
