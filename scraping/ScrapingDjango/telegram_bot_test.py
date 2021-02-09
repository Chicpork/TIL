import os
import logging
import logging.config
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update, Bot

# make logger
with open("logging.json", "r") as f:
    config = json.load(f)

logging.config.dictConfig(config)
logger = logging.getLogger("base")

# telegram bot info
with open('./secured/config.json') as f:
    config = json.load(f)
    telegram_bot_info = config["TELEGRAM_BOT_INFO"]

# start command handlers
def start(update: Update, context: CallbackContext):
    logger.info("start Handler Start...")
    context.bot.send_message(chat_id=telegram_bot_info["BOT_CHAT_ID"], text="Bot Start!")

# stop command handlers
def stop(update: Update, context: CallbackContext):
    logger.info("stop Handler Start...")
    context.bot.send_message(chat_id=telegram_bot_info["BOT_CHAT_ID"], text="Bot Stop!")

# undefined command handlers
def unknown(update: Update, context: CallbackContext):
    logger.info("unknown Handler Start...")
    context.bot.send_message(chat_id=telegram_bot_info["BOT_CHAT_ID"], text="unknown command")

# search command
def search(update: Update, context: CallbackContext):
    logger.info("search Handler Start...")

    if len(context.args) != 3:
        context.bot.send_message(chat_id=telegram_bot_info["BOT_CHAT_ID"], text="Please type like \"/search site minPrice maxPrice\"")
    
    site = context.args[0]
    min_price = context.args[1]
    max_price = context.args[2]
    
    message = "Crawling Start.. [site : " + site + ", min_price : " + min_price + ", max_price : " + max_price + "]"
    context.bot.send_message(chat_id=telegram_bot_info["BOT_CHAT_ID"], text=message)
    # exec()
    # os.getpid()

def echo(update: Update, context: CallbackContext):
    logger.info("echo Handler Start...")
    context.bot.send_message(chat_id=telegram_bot_info["BOT_CHAT_ID"], text=update.channel_post.text)

def main():
    updater = Updater(telegram_bot_info["BOT_TOKEN"])

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(MessageHandler(Filters.command, unknown))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('stop', stop, pass_args=True))
    dp.add_handler(CommandHandler('search', search, pass_args=True))
    
    # Run until stop
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()