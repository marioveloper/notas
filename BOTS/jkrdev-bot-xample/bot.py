from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('hola humano')

if __name__ == '__main__':

    updater = Updater(token='', use_context=True)

    dp = updater.dispatcher

    #add handler
    dp.add_handler(CommandHandler('start', start))

    #esta en constante escucha
    updater.start_polling()
    updater.idle()