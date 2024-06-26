import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def cmd_start(message):
    text = f'Hola {message.from_user.username}, como estas'
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def receive_text(message):
    text = message.text
    if message.text.startswith('/'):
        text = 'Solo los administradores pueden enviar comandos'
    elif message.text.__contains__('referidos'):
        text = f'Tienes un referido'
    bot.send_message(message.chat.id, text)

if __name__ == '__main__':
    print('Iniciando Bot....')
    bot.polling()