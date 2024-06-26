import telebot
import mysql.connector
from config import *

bot = telebot.TeleBot(TOKEN)
conexion = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, port=PORT, database=DATABASE)
cursor = conexion.cursor()

@bot.message_handler(commands=['start'])
def cmd_start(message):
    telegram_id = message.from_user.id
    firstname = message.from_user.first_name
    username = message.from_user.username
    referred_by = message.text
    referred_by = referred_by.strip('/start ')
    invite_link = f'https://t.me/stainedpruebabot?start={telegram_id}'

    #consulta
    query = f'INSERT INTO users(telegram_id, firstname, username, referred_by, invite_link) \
    VALUES (%s, %s, %s, %s, %s)'
    parameters = (telegram_id, firstname, username, referred_by, invite_link)
    try:
        cursor.execute(query, parameters)
        conexion.commit()
    except ConnectionError as e:
        print(e)

    #bienvenida
    text=f'Hola {firstname}, bienvenido a Stained Glass\nEste es tu enlace de invitacion: {invite_link}'
    bot.reply_to(message, text=text)

@bot.message_handler(commands=['cuenta'])
def cmd_Account(message):
    id = message.from_user.id
    query = f'SELECT * FROM users WHERE telegram_id = %s'
    parameters = (id,)

    try:
        tabla = cursor.execute(query, parameters)
        tabla = cursor.fetchall()

        id = tabla[0][0]
        telegram_id = tabla[0][1]
        firstname = tabla[0][2]
        username = tabla[0][3]
        if username == None:
            username = ''

        referred_by = tabla[0][4]
        if referred_by == '':
            referred_by = 'Nadie'

        invite_link = tabla[0][5]

        rank = tabla[0][6]
        if rank == 'none':
            rank = 'Aun necesitas invitar amigos'
        wallet = tabla[0][7]
        if wallet == 'none':
            wallet = 'No establecida'

        referrals = tabla[0][8]

        status = tabla[0][9]
        if status == 0:
            status = 'Aun no has realizado ninguna compra'

        active = tabla[0][10]
        if active == 0:
            active = 'No tienes planes activos'
        if active == 1:
            active = 'compra realizada el.....'

        my_cuenta = f'Nombre: <i>{firstname}</i>\n\nNombre de Usuario: <i>@{username}</i>\n\nEnlace de invitacion: <i>{invite_link}</i>\n\nRango: <i>{rank}</i>\n\nReferidos: <i>{referrals}</i>\n\nWallet: <i>{wallet}</i>\n\n<i>{status}\n{active}</i>'
    except ConnectionError as e:
        print(e)

    bot.reply_to(message, text=my_cuenta, parse_mode="HTML")

    if referrals > 0:
        try:
            query = f'SELECT firstname, username, rank, referrals, active FROM users WHERE referred_by = %s and status = 1'
            parameters = (telegram_id,)

            tabla = cursor.execute(query, parameters)
            tabla = cursor.fetchall()
            referidos = f'<b>Referidos:</b>\n\n'
            for filas in tabla:
                    referidos += 'Nombre: <i>'
                    referidos += str(filas[0])
                    referidos += '</i>\n'

                    referidos += 'Nombre de usuario: <i>@'
                    if str(filas[1])==None:
                        referidos += str(filas[1])
                    else:
                        referidos +=''
                    referidos += '</i>\n'

                    referidos += 'Rango: <i>'
                    referidos += str(filas[2])
                    referidos += '</i>\n'

                    referidos += 'Referidos: <i>'
                    referidos += str(filas[3])
                    referidos += '</i>\n'

                    referidos += 'Activo: <i>'
                    if filas[4]==0:
                        referidos += 'No</i>\n\n'
                    else:
                        referidos += 'Si</i>\n\n'
        except ConnectionError as e:
            print(e)

        bot.send_message(telegram_id, text=referidos, parse_mode="HTML")

@bot.message_handler(commands=['wallet'])
def cmd_wallet(message):
    id = message.from_user.id
    wallet = message.text.split()
    text = ''
    if len(wallet)>1:
        if wallet[1].isalnum():
            try:
                query = f'UPDATE users SET wallet = %s WHERE telegram_id = %s'
                parameters = (wallet[1], message.from_user.id)
                cursor.execute(query, parameters)
                conexion.commit()
                text = f'Wallet Actualizada a "{wallet[1]}"'
            except ConnectionError as e:
                print(e)
        else:
            text = 'Formato Incorrecto\nPara establecer una nueva wallet debe enviar un mensaje con el formato siguiente: \n/wallet direcciondelawallet\nejemplo:\n\n'
            text += '/wallet 0x7f22615B96400899f8CFE09580C4B6f9d49fFF77'
            print(wallet)
    else:
        text += 'La wallet no puede estar Vacia'
        text += '\nPara establecer una nueva wallet debe enviar un mensaje con el formato siguiente: \n/wallet direcciondelawallet\n\nEjemplo:\n'
        text += '/wallet 0x7f22615B96400f9d49fFF77'
    bot.reply_to(message, text=text)

@bot.message_handler(commands=['comprarplan'])
def cmd_plan(message):
    text = 'Para comprar su plan transfiera 30USDT a la siguiente wallet:\n\n'
    text += PAYMENTS_WALLET
    text += '\n\nLuego envie una captura de pantalla de la transaccion realizada, con el texto "prueba de pago".\n\nUna vez los administradoes comprueben su pago, usted será notificado'
    bot.reply_to(message, text=text)


@bot.message_handler(commands=['adminVerPagos'])
def admin_verPagos(message):

    if ADMIN_ID.__contains__(str(message.from_user.id)):
        query = 'SELECT user_id, date FROM investments WHERE success = 0 ORDER BY date'
        try:
            tabla = cursor.execute(query)
            tabla = cursor.fetchall()
            text = 'PAGOS'
            for fila in tabla:
                text+='\n\n<b>User_id:</b> '
                text+=str(fila[0])
                text+='\n<b>Fecha:</b> '
                text+=str(fila[1])

        except ConnectionError as e:
            print(e)
    else:
        text = 'Comando Desconocido\n\nComandos Disponibles\n\n/cuenta Muestra informacion sobre tu cuenta\n/wallet para modificar la wallet(billetera)\n\n/comprarplan para comprar un plan'
    bot.reply_to(message, text=text, parse_mode='HTML')

@bot.message_handler(content_types=['text'])
def receive_text(message):
    text = message.text
    if message.text.startswith('/'):
        text = 'Comando Desconocido'
    else:
        text= 'Stained Glass bot'
    text +='\n\nComandos Disponibles\n\n/cuenta Muestra informacion sobre tu cuenta\n/wallet para modificar la wallet(billetera)\n\n/comprarplan para comprar un plan'
    bot.reply_to(message, text=text)


if __name__ == '__main__':
    print('escuchando....')
    bot.infinity_polling()