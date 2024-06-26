import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def cmd_start(message):
    telegram_id = message.from_user.id
    firstname = message.from_user.first_name
    username = message.from_user.username
    referred_by = message.text
    referred_by = referred_by.strip('/start ')
    invite_link = f'https://t.me/stainedpruebabot?start={telegram_id}'

    #bienvenida
    text=f'Hola {firstname}, bienvenido a Stained Glass\nEste es tu enlace de invitacion: {invite_link}'
    bot.reply_to(message, text=text)

@bot.message_handler(commands=['cuenta'])
def cmd_Account(message):
    id = message.from_user.id

    bot.reply_to(message, text=my_cuenta, parse_mode="HTML")

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