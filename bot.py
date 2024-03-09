from typing import Final
from telegram import Update
from telegram.ext import Application, commandHandler, messageHandler, filters, contextTypes
TOKEN: Final="7121693986:AAFwYTxclMjFeP6ipNj8MKJ0_hy1bWlHCU8"
BOT_USERNAME: Final = '@KKanilabot'



#commands
async def start_command(update: update, context: contextTypes.DEFAULT_TYPE):

await update.message.reply_text("Hi am kkanila thank you for chatting")

async def help_command(update: update, context: contextTypes.DEFAULT_TYPE):
await update.message.reply_text("please type something so that i can respond")


async def custom_command(update: update, context: contextTypes.DEFAULT_TYPE):
await update.message.reply_text("this is a custom command")


#Responses

def handle_