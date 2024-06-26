
from telegram import Update, ParseMode, ChatAction
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from urllib.request import urlopen

TOKEN = "1891174386:AAGYArFVDYwhhbwVFV1cqZuFHisXIovDB-A"
CHAT_ID = 292874486

# Handlers
def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    print(update.message.chat.id)
    update.message.reply_text(update.message.text, reply_to_message_id=update.message.message_id)


def main() -> None:
    """Start the bot."""
    # Creamos Updater y le pasamos el token
    updater = Updater(TOKEN)

    # Obtenemos el dispatcher para registrar los handlers
    dispatcher = updater.dispatcher

    # Handler para eco
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    #Proactive
    updater.bot.send_message(CHAT_ID, "Hola que tal, soy proactivo?")

    # Iniciar el bot
    updater.start_polling()

    #Mantener el proceso hasta que se pulse Ctrl + C
    updater.idle()


if __name__ == '__main__':
    main()