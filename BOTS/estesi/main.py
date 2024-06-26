import telebot
import mysql.connector
import time, datetime
from config import *
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ForceReply
from funciones import *

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

    query = f'SELECT id FROM users WHERE telegram_id = %s'
    parameters = (telegram_id,)
    try:
        usuario = cursor.execute(query, parameters)
        usuario = cursor.fetchall()
        if not usuario:
            #consulta
            query = f'INSERT INTO users(telegram_id, firstname, username, referred_by, invite_link) \
            VALUES (%s, %s, %s, %s, %s)'
            parameters = (telegram_id, firstname, username, referred_by, invite_link)
            try:
                cursor.execute(query, parameters)
                conexion.commit()
            except ConnectionError as e:
                print(e)
    except ConnectionError as e:
        print(e)

    #bienvenida
    text=f'Hola {firstname}, bienvenido a Stained Glass\nEste es tu enlace de invitacion: {invite_link}'

    bot.send_message(message.chat.id, text=text, reply_markup=dibujar_teclado(message.chat.id))

@bot.message_handler(content_types=['text'])
def receive_text(message):
    text = message.text
    print(message.chat.id, text)

    ###===================Comandos Usuarios=======================##

    #Comando mi Cuenta
    if message.text == 'Mi Cuenta':
        id = message.from_user.id
        actualizar_rango(id)
        query = f'SELECT * FROM users WHERE telegram_id = %s'
        parameters = (id,)
        text = 'Ocurrio un error, Reintenta'
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
            else:
                status = 'Activo'
            active = tabla[0][10]
            if active == 0:
                active = 'No tienes planes activos'
            if active == 1:
                date = cursor.execute(f'SELECT date FROM investments WHERE user_id = {id} and success = 0 ORDER BY id DESC limit 1')
                date = cursor.fetchall()
                active = f'compra realizada {date[0][0]}'
            text = f'Nombre: <i>{firstname}</i>\n\nNombre de Usuario: <i>@{username}</i>\n\nEnlace de invitacion: <i>{invite_link}</i>\n\nRango: <i>{rank}</i>\n\nReferidos: <i>{referrals}</i>\n\nWallet: <i>{wallet}</i>\n\n<i>{status}\n{active}</i>'
        except ConnectionError as e:
            print(e)
        bot.reply_to(message, text=text, parse_mode="HTML", reply_markup=dibujar_teclado(message.chat.id))

    #Mis Referidos
    if message.text == 'Mis Referidos':
        try:
            query = f'SELECT firstname, username, referrals FROM users WHERE referred_by = %s'
            parameters = (message.chat.id,)
            tabla = cursor.execute(query, parameters)
            tabla = cursor.fetchall()
            text = 'Referidos:'
            for fila in tabla:
                text+='\n\nNombre: <i>'
                text+=(fila[0])
                text+='</i>\nUsuario: <i>@'
                text+=str(fila[1])
                text+='</i>\nReferidos: <i>'
                text+=str(fila[2])
                text+='</i>'
            bot.reply_to(message,text=text, reply_markup=dibujar_teclado(message.chat.id),parse_mode='HTML')
        except ConnectionError as e:
            print(e)

    #Modificar Wallet
    if message.text == 'Modificar Wallet':
        teclado =ReplyKeyboardMarkup(resize_keyboard=True)
        teclado.add('Cancelar')
        text = 'Introduce tu Wallet'
        wallet = bot.send_message(message.chat.id, text=text, reply_markup=teclado)
        bot.register_next_step_handler(wallet, registrar_wallet)

    #Comprar Plan
    if message.text == 'Comprar Plan':
        teclado =ReplyKeyboardMarkup(resize_keyboard=True)
        teclado.add('Cancelar')
        text = f'1. Transfiere 30USDT a la siguiente wallet: {PAYMENTS_WALLET}\n2. Envia una captura de pantalla donde muestre la transaccion realizada'
        mensaje = bot.send_message(message.chat.id, text=text, reply_markup=teclado)
        bot.register_next_step_handler(mensaje, registrar_pago)

    #Reglas
    if message.text == 'REGLAS':
        text = '“But I must explain to you how all this mistaken idea of denouncing of a pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?”'
        bot.reply_to(message, text=text, reply_markup=dibujar_teclado(message.chat.id))

    ###===============COMANDOS ADMINISTRADORES===============###

    #Admin Ver Pagos
    if message.text == 'Ver Pagos':
        if ADMIN_ID.__contains__(str(message.chat.id)):
            try:
                query = 'SELECT user_id, date FROM investments WHERE succes = 0 ORDER BY date'
                tabla = cursor.execute(query)
                tabla = cursor.fetchall()
                text = 'Pagos'
                for fila in tabla:
                    text += '\n\nUser_id:  '
                    text += str(fila[0])
                    text += '\nDate:  '
                    text += str(fila[1])
                bot.reply_to(message, text=text)
            except ConnectionError as e:
                print(e)

    #Admin Insertar Pago
    if message.text == 'InsertarPago':
        if ADMIN_ID.__contains__(str(message.chat.id)):
            teclado =ReplyKeyboardMarkup(resize_keyboard=True)
            teclado.add('Cancelar')
            mensaje = bot.send_message(message.chat.id, text='Coloque el ID: ', reply_markup=teclado)
            bot.register_next_step_handler(mensaje, admin_insertarpago)

    #Admin Finalizar Plan
    if message.text == 'Finalizar Plan':
        if ADMIN_ID.__contains__(str(message.chat.id)):
            teclado =ReplyKeyboardMarkup(resize_keyboard=True)
            teclado.add('Cancelar')
            mensaje = bot.send_message(message.chat.id, text='Coloque el ID: ', reply_markup=teclado)
            bot.register_next_step_handler(mensaje, admin_finalizarplan)

    #Admin Consultar Usuario
    if message.text == 'Consultar Usuario':
        if ADMIN_ID.__contains__(str(message.chat.id)):
            teclado =ReplyKeyboardMarkup(resize_keyboard=True)
            teclado.add('Cancelar')
            mensaje = bot.send_message(message.chat.id, text='Coloque el telegram_ID: ', reply_markup=teclado)
            bot.register_next_step_handler(mensaje, admin_consultarusuario)

    #Admin Listar Usuarios
    if message.text == 'Listar Usuarios':
        if ADMIN_ID.__contains__(str(message.chat.id)):
            query = 'SELECT * FROM users ORDER BY id'
            try:
                tabla = cursor.execute(query)
                tabla = cursor.fetchall()
                text = 'Usuarios'
                for fila in tabla:
                    text += 'ID: '
                    text+= str(fila[0])
                    text+= '\ntelegram_id: '
                    text+= str(fila[1])
                    text+= '\nnombre: '
                    text+= str(fila[2])
                    text+= '\nusername: @'
                    text+= str(fila[3])
                    text+= '\nreferido por: '
                    text+= str(fila[4])
                    text+= '\nlink: '
                    text+= str(fila[5])
                    text+= '\nrango: '
                    text+= str(fila[6])
                    text+= '\nwallet: '
                    text+= str(fila[7])
                    text+= '\nreferidos: '
                    text+= str(fila[8])
                    text+= '\nestado: '
                    text+= str(fila[9])
                    text+= '\nactivo: '
                    text+= str(fila[10])
                    text+= '\n\n'
                mensaje = bot.reply_to(message, text=text, reply_markup=dibujar_teclado(message.chat.id))
            except ConnectionError as e:
                print(e)

    #manejar cancelar general
    if message.text == 'Cancelar':
        bot.send_message(message.chat.id,text='Cancelado', reply_markup=dibujar_teclado(message.chat.id))

#====================FUNCIONES USUARIOS==================#
def registrar_wallet(message):
    if message.text == None:
        text = 'Formato de Wallet Incorrecto\nIntroduce tu wallet'
        teclado =ReplyKeyboardMarkup(resize_keyboard=True)
        teclado.add('Cancelar')
        wallet = bot.send_message(message.chat.id, text=text, reply_markup=teclado)
        bot.register_next_step_handler(wallet, registrar_wallet)
    else:
        if message.text.isalnum():
            try:
                query = f'UPDATE users SET wallet = %s WHERE telegram_id = %s'
                #query = f'UPDATE users SET rank = %s WHERE telegram_id = %s'
                parameters = (message.text, message.from_user.id)
                cursor.execute(query, parameters)
                conexion.commit()
                text = f'Wallet Actualizada a "{message.text}"'
            except ConnectionError as e:
                print(e)
            bot.reply_to(message, text=text, reply_markup=dibujar_teclado(message.chat.id))
        else:
            text = 'Formato de Wallet Incorrecto\nIntroduce tu wallet'
            teclado =ReplyKeyboardMarkup(resize_keyboard=True)
            teclado.add('Cancelar')
            wallet = bot.send_message(message.chat.id, text=text, reply_markup=teclado)
            bot.register_next_step_handler(wallet, registrar_wallet)

def registrar_pago(message):
    if message.text == 'Cancelar':
        bot.send_message(message.chat.id, text='Cancelado', reply_markup=dibujar_teclado(message.chat.id))
    else:
        if message.content_type == 'photo':
            text = f'Su captura ha sido recibida, cuando sea validada usted sera notificado'
            bot.reply_to(message, text=text, reply_markup=dibujar_teclado(message.chat.id))
            bot.send_message(CHANNEL_PAGOS, text=f'Prueba Pago\n{message.chat.id}')
            time.sleep(1)
            bot.forward_message(CHANNEL_PAGOS, message.chat.id, message.message_id)
        else:
            text = f'Debe enviar una imagen'
            teclado=ReplyKeyboardMarkup(resize_keyboard=True)
            teclado.add('Cancelar')
            mensaje = bot.send_message(message.chat.id, text=text, reply_markup=teclado)
            bot.register_callback_query_handler(mensaje, registrar_pago)

#FUNCIONES ADMINISTRADORES
def admin_insertarpago(message):
    if message.content_type == 'text':
        if message.text == 'Cancelar':
            bot.send_message(message.chat.id, text='Cancelado', reply_markup=dibujar_teclado(message.chat.id))
        else:
            if message.text.isnumeric():
                try:
                    id = cursor.execute(f'SELECT id FROM users WHERE telegram_id = {message.text}')
                    id = cursor.fetchall()
                    if id:
                        id=id[0]
                        id=id[0]
                        query=f'INSERT INTO investments(date, user_id) VALUES (%s, %s)'
                        parameters = (datetime.datetime.now(), id)
                        cursor.execute(query, parameters)
                        conexion.commit()
                        activar_usuario(str(id))
                        bot.send_message(message.text, text='Su pago ha sido aceptado', reply_markup=dibujar_teclado(message.text))
                        bot.send_message(message.chat.id, text='Guardado con exito', reply_markup=dibujar_teclado(message.chat.id))
                    else:
                        bot.send_message(message.chat.id, text='No existe un usuario con ese id', reply_markup = dibujar_teclado(message.chat.id))
                except ConnectionError as e:
                    print(e)

def admin_finalizarplan(message):
    if message.content_type == 'text':
        if message.text == 'Cancelar':
            bot.send_message(message.chat.id, text='Cancelado', reply_markup=dibujar_teclado(message.chat.id))
        else:
            if message.text.isnumeric():
                try:
                    id = cursor.execute(f'SELECT id FROM users WHERE id = {message.text}')
                    id = cursor.fetchall()
                    if id:
                        query=f'UPDATE investments SET succes = 1 WHERE user_id = %s'
                        parameters = (message.text,)
                        cursor.execute(query, parameters)
                        conexion.commit()
                        desactivar_usuario(message.text)
                        bot.send_message(message.chat.id, text='Guardado con exito', reply_markup=dibujar_teclado(message.chat.id))
                    else:
                        bot.send_message(message.chat.id, text='No existe un usuario con ese id', reply_markup=dibujar_teclado(message.chat.id))
                except ConnectionError as e:
                    print(e)

def admin_consultarusuario(message):
    if message.content_type == 'text':
        if message.text == 'Cancelar':
            bot.send_message(message.chat.id, text='Cancelado', reply_markup=dibujar_teclado(message.chat.id))
        else:
            if message.text.isnumeric():
                try:
                    tabla = cursor.execute(f'SELECT * FROM users WHERE telegram_id = %s', (message.text,))
                    tabla = cursor.fetchall()
                    if not tabla:
                        tabla = cursor.execute(f'SELECT * FROM users WHERE id = %s', (message.text,))
                        tabla = cursor.fetchall()
                    text = 'ID: '
                    text+= str(tabla[0][0])
                    text+= '\ntelegram_id: '
                    text+= str(tabla[0][1])
                    text+= '\nnombre: '
                    text+= str(tabla[0][2])
                    text+= '\nusername: @'
                    text+= str(tabla[0][3])
                    text+= '\nreferido por: '
                    text+= str(tabla[0][4])
                    text+= '\nlink: '
                    text+= str(tabla[0][5])
                    text+= '\nrango: '
                    text+= str(tabla[0][6])
                    text+= '\nwallet: '
                    text+= str(tabla[0][7])
                    text+= '\nreferidos: '
                    text+= str(tabla[0][8])
                    text+= '\nestado: '
                    text+= str(tabla[0][9])
                    text+= '\nactivo: '
                    text+= str(tabla[0][10])

                    bot.send_message(message.chat.id, text=text, reply_markup=dibujar_teclado(message.chat.id))
                except ConnectionError as e:
                    print(e)

#===========FUNCIONES GENERALES DEL BOT==============###
def dibujar_teclado(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('REGLAS')
    markup.add('Mi Cuenta', 'Mis Referidos')
    markup.add('Modificar Wallet','Comprar Plan')
    if ADMIN_ID.__contains__(str(id)):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Listar Usuarios')
        markup.add('Ver Pagos', 'InsertarPago')
        markup.add('Finalizar Plan', 'Consultar Usuario')

    return markup

#esta queda por modificarse
def actualizar_datos(telegram_id,firstame,username):
    cursor.execute(f'UPDATE users SET firstname = {firstname} WHERE telegram_id = {telegram_id}')
    cursor.execute(f'UPDATE users SET username = {username} WHERE telegram_id = {telegram_id}')
    conexion.commit()

#arreglar
def actualizar_rango(id):
    try:
        query = f'SELECT id, referrals FROM users WHERE telegram_id = {id}'
        tabla = cursor.execute(query)
        tabla = cursor.fetchall()
        tabla = tabla[0]
        #id = tabla[0]
        referrals = tabla[1]
        #print(id, referrals)
        #referrals = referrals[0]
        rank = colocar_rango(referrals)
        parameters = (rank, id)
        print(type(id), type(rank))
        query = f'UPDATE users SET rank = %s WHERE telegram_id = %s'
        cursor.execute(query, parameters)
        conexion.commit()

    except ConnectionError as e:
        print(e)

if __name__ == '__main__':
    print('escuchando')
    bot.infinity_polling()