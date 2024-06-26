import os
import sys
import logging
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(
    leve=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,"
)
logger = logging.getLogger()

TOKEN = os.getenv("TOKEN")
#otras funciones
def deleteMessage(bot, chatId, messageId, userName):
    try:
        bot.delete_message(chatId, messageId)
        logger.info(f'El mensaje de {userName} se elimino correctamente')
    except Exception as e:
        print(e)

#funciones de los comandos
def getBotInfo(update, context):
    bot = context.box
    chatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    logger.info(f'El usuario {userName} ha solicitado informacion sobre el bot')
    bot.sendMessage(
        chat_id = chatId,
        parse_mode = "HTML",
        text = f'Hola soy un bot creado para el canal de <b>mario</b>'
    )

def start(update, context):
    bot = bot.context
    userName = update.effective_user["first_name"]
    update.message.reply_text(f'Hola {userName} bienvenido')

def welcomeMsg(update, context):
    bot = context.bot
    chatId = update.message.chat_id
    updateMsg = getattr(update, "message", None)

    for user in updateMsg.new_chat_members:
        userName = user.first_name

    logger.info(f'el usuario {userName} ha ingresado al grupo')

    bot.send_message(
        chat_id = chatId,
        parse_mode = "HTML",
        text = f'<b>Bienvenido al grupo {userName}</b>'
    )

def echo(update, context):
    bot = context.bot
    updateMsg = getattr(update, 'message', None)
    messageId = updateMsg.message_id #id del mensaje
    chatId = update.message.chat_id
    userName = update.effective_user['first_name']
    text = update.message.text #obtener el texto q encvio el usuario al chat
    logger.info(f'El usuario {userName} ha enviado un mensaje al grupo {chatId}')

    badWord = 'baboso'

    if badWord in text:
        deleteMessage(bot, chatId, messageId, userName)
        bot.sendMessage(
            chat_id=chatId,
            text=f'El mensaje de {userName} ha sido eliminado'
        )
    elif 'bot' in text and 'hola' in text:
        bot.sendMessage(
            chat_id=chatId,
            text=f'gracias por saludar {userName} '
        )

if __name__ == "__main__":
    #obtener informacion del bot
    mybot = telegram.Bot(token=TOKEN)
    #print(mybot.getMe())


#upadater
updater = Updater(mybot.token, use_context=True)


#crear despachador
dp = updater.dispatcher

#crear manejador( comando)
dp.add_handler(CommandHandler("botInfo", getBotInfo))
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcomeMsg))
dp.add_handler(MessageHandler(Filters.text, echo))

#polling
updater.start_polling()
print('Bot running')
#idle terminar bot con ctrol + c
updater.idle()