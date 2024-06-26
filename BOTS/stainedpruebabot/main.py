import telebot
import conexion as conn

#--------------variables-----------------#

TOKEN = '5483226127:'
db = conn.DB()
bot = telebot.TeleBot(TOKEN)

#---------------comandos-----------------#

#------start-----#
@bot.message_handler(commands=['start'])
def send_welcome(message):
    #variables
    id = message.from_user.id
    firstname = message.from_user.first_name
    username = message.from_user.username
    padre = message.text[-10:-1]
    padre = padre.strip('/start')
    invite_link = f'https://t.me/stainedpruebabot?start={id}'



    #consulta
    query = f'INSERT INTO user(id, firstname, username, padre, chat_id, chat_type, has_private_forwards, invite_link, saldo, numero_telefonico, tarjeta) \
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    parameters = (id, firstname, username, padre, chat_id, chat_type, has_private_forwards, invite_link, saldo, numero_telefonico, tarjeta)
    try:
        db.execute_query(query, parameters)
    except:
        print('usuario en existencia')

    #bienvenida
    text=f'Hola {firstname}, {invite_link} este es tu link de invitacion'
    bot.reply_to(message, text=text)

#-----help------#
@bot.message_handler(commands=['help'])
def send_help(message):
    text = 'Bot creado con caracter comercial por Mario Luis\
        \nsi desea un bot parecido puede encontrarme en telegram como @jkr_web, @jkr_admin o @jkr_dev\
        \ncualquier fallo en el bot tambien puede contactarme'
    bot.reply_to(message, text=text)

#-----rules-----#
@bot.message_handler(commands=['rules'])
def send_rules(message):
    text = 'En este bot podras jugar a la bolita cubana\
        \nEl numero se toma del sitio web labolitacubana.com\
        \nLos pagos son:\
        \n1x70 la decena\
        \n1x200 la centena\
        \n1x25 el parlet\
        \nLos pagos se realizan en automatico\
        '
    bot.reply_to(message, text=text)

#-----myAccount------#
@bot.message_handler(commands=['myAccount'])
def send_help(message):
    id = message.from_user.id
    query = 'SELECT * FROM user WHERE id = ?'
    parameters = (id,)
    try:
        result = db.execute_query(query, parameters)
        result = result.fetchall()
        print(result)
        saldo = result[0][8]
        text = f'Tu saldo es: {saldo}'
        bot.reply_to(message, text=text)
    except:
        bot.reply_to(message, text='ocurrio un error')



print('bot a la escucha')
bot.polling()