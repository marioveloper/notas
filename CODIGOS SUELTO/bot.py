import telebot

bot = telebot.TeleBot("5271671442:AAGtBpG0B9miaBegICd1Ay-KCRRY6icMjQg")
@bot.message_handler(commands=["help", "start"])

def enviar(message):
    bot.reply_to(message, "Hola, Como estas?")


@bot.message_handler(func=lambda message:True)

def mensaje(message):
    bot.reply_to(message, message.text)

bot.polling()