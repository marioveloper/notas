import telebot
import conexion as conn



#--------------variables-----------------#

TOKEN = '5483226127:AAHcZVSPQUTO_nla6uNm71B7j6MAZ0r_8UA'
db = conn.DB()
bot = telebot.TeleBot(TOKEN)

#---------------comandos-----------------#

@bot.message_handler(commands=['start'])
def send_welcome(message):
    #variables
    id = message.from_user.id
    firstname = message.from_user.first_name
    username = message.from_user.username
    referred_by = message.text
    referred_by = referred_by.strip('/start ')
    invite_link = f'https://t.me/stainedpruebabot?start={id}'


    #consulta
    query = f'INSERT INTO user(id, firstname, username, referred_by, invite_link) \
    VALUES (?, ?, ?, ?, ?)'
    parameters = (id, firstname, username, referred_by, invite_link)
    try:
        db.execute_query(query, parameters)
    except ConnectionError as e:
        print(e)

    #bienvenida
    text=f'Hola {firstname}, bienvenido a Stained Glass\nEste es tu enlace de invitacion: {invite_link}'
    bot.reply_to(message, text=text)

@bot.message_handler(commands=['myAccount'])
def send_Account(message):
    id = message.from_user.id
    query = f'SELECT firstname, username, referrals, rank, invite_link, status FROM user WHERE id = ?'
    parameters = (id,)

    try:
        tabla = db.execute_query(query, parameters).fetchone()
        text = 'My Account\n'
        text+='Firstname: '
        text += tabla[0]
        text+='\n'
        text+='Username: @'
        text+=tabla[1]
        text+='\n'
        text+='Referrals: '
        if tabla[2]==0:
            text+='Debes Invitar Amigos'
        else:
            text+=str(tabla[2])
        text+='\n'
        text+='Rank: '
        if tabla[3]==None:
            text+='Aun no alcanzas el primer rango'
        else:
            text+=tabla[3]
        text+='\n'
        text+='Invite Link: '
        text+=tabla[4]
        text+='\n'
        text+='Status: '
        if tabla[5]==1:
            query2 = 'SELECT date FROM investments WHERE user_id = ? ORDER BY id DESC LIMIT 1'
            parameters2 = (id,)
            text += 'Active\n'
            try:
                tabla2 = db.execute_query(query2, parameters2).fetchone()
                text+='Compra Realizada en '
                text+=tabla2[0]
            except ConnectionError as e:
                print(e)
        else:
            text += 'Inactive'


    except ConnectionError as e:
        print(e)

    bot.reply_to(message, text=text)

@bot.message_handler(commands=['myReferrals'])
def send_referrals(message):
    id = message.from_user.id
    query = f'SELECT firstname, username, status FROM user WHERE referred_by = ? ORDER BY status DESC'
    parameters = (id,)
    try:
        tabla = db.execute_query(query, parameters).fetchall()
        text = f'My Referrals: \n\n'
        text += 'Total: '
        text +=str(len(tabla))
        text+='\n\n'
        for row in tabla:
            text+='Firstname: '
            text+=row[0]
            text+='\n'
            text+='Username: @'
            text+=row[1]
            text+='\n'
            if row[2]==0:
                text+='Status: Inactive\n'
            else:
                text+='Status: Active\n'
            text+='\n'
    except ConnectionError as e:
        print(e)

    bot.reply_to(message, text=text)

@bot.message_handler(commands=['realicePay'])
def realice_pay(message):

    import datetime
    admin_id = message.from_user.id
    user_id = message.text.replace('/realicePay', '')
    date = datetime.datetime.now()

    query = 'SELECT id FROM investments WHERE id = ?'
    parameters = (user_id,)

    try:
        tabla = db.execute_query(query, parameters).fetchone()
        if tabla == ():
            query2 = 'INSERT INTO investments(date, user_id) VALUES (?,?)'
            parameters2 = (date, user_id)
            try:
                db.execute_query(query2,parameters2)
                #seleccionar a actualizar cantidad referidis
            except ConnectionError as e:
                print(e)

    except ConnectionError as e:
        print(e)
print('bot a la escucha')
bot.polling()