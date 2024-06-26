from asyncio.log import logger
import os
from pickle import TRUE
import sys
import logging
from tracemalloc import start
from matplotlib.pyplot import text
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(
    leve=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,"
)
logger = logging.getLogger()

TOKEN = os.getenv("TOKEN")

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



if __name__ == "__main__":
    #obtener informacion del bot
    mybot = telegram.Bot(token=TOKEN)
    #print(mybot.getMe())


#upadater
updater = Updater(mybot.token, use_context=TRUE)


#crear despachador
dp = updater.dispatcher

#crear manejador( comando)
dp.add_handler(CommandHandler("botInfo", getBotInfo))
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcomeMsg))


#polling
updater.start_polling()
print('Bot running')
#idle terminar bot con ctrol + c
updater.idle()