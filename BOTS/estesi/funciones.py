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

def colocar_rango(referrals):
    if referrals == 3:
        return "Peon Blanco ⭐️"
    if referrals == 5:
        return 'Peon Negro ⭐️'
    if referrals == 10:
        return 'Peon Blanco ⭐️⭐️'
    if referrals == 15:
        return 'Peon Negro ⭐️⭐️'
    if referrals == 20:
        return 'Peon Blanco ⭐️⭐️⭐️'
    if referrals == 40:
        return 'Peon Negro ⭐️⭐️⭐️'
    if referrals == 80:
        return 'Torre Blanca ⭐️'
    if referrals == 120:
        return 'Torre Negra ⭐️⭐️'
    if referrals == 160:
        return 'Caballo Blanco ⭐️'
    if referrals == 200:
        return 'Caballo Negro ⭐️⭐️'
    if referrals == 240:
        return 'Alfil Blanco ⭐️'
    if referrals == 500:
        return 'Alfil Negro ⭐️⭐️'
    if referrals == 750:
        return 'Reina Blanca ⭐️⭐️⭐️⭐️'
    if referrals == 1000:
        return 'Rey Negro ⭐️⭐️⭐️⭐️⭐️'