
from telegram import Update, ParseMode
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

TOKEN = "1891174386:AAGYArFVDYwhhbwVFV1cqZuFHisXIovDB-A"

# Handlers
def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_audio(open("\\bateria.mp3", 'rb'), title="Playing drums", performer="Mario Luis", reply_to_message_id=update.message.message_id,
        caption = "Mi primer audio", thumb = open("\\bateria.jpg", 'rb'))


def main() -> None:
    """Start the bot."""
    # Creamos Updater y le pasamos el token
    updater = Updater(TOKEN)

    # Obtenemos el dispatcher para registrar los handlers
    dispatcher = updater.dispatcher

    # Handler para eco
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Iniciar el bot
    updater.start_polling()

    #Mantener el proceso hasta que se pulse Ctrl + C
    updater.idle()


if __name__ == '__main__':
    main()