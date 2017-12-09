#!/usr/bin/python3

from uuid import uuid4
import re
import telegram
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, CallbackQueryHandler, ConversationHandler, Filters
import logging
import argparse
# Command modules
import commands.cmdFAQ as FAQ
import commands.cmdNET as NET

method = ''
token = ''

logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)



def help(bot, update):
	help_message = "I'm an informative Bot for the Nimiq Community.\n\n\
			USAGE:\n\n\
			/question Input your question.\n\
			Input your question and I'll try to answer it.\n\n\
			/net\n\
                        General information about Nimiq.\n\n\
			/net address\n\
			Gives the balance of a specific address.\n\n\
			/net contributors\n\
			Gives information about the amount of contributors."
	bot.sendMessage(update.message.chat_id, text=help_message)

def error(bot, update, error):
	logger.warn('Update "%s" caused error "%s"' % (update, error))

def unknown(bot, update):
	bot.sendMessage(update.message.chat_id, text="Unknown command... (/help)")

def main():
	import yaml
	cfg_file = './config/botcfg.yml'
	with open(cfg_file, 'r') as ymlfile:
		cfg = yaml.load(ymlfile)
	token = cfg['token']
	bot = telegram.Bot(token=token)
	updater = Updater(token)
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("help", help))
	dp.add_handler(CommandHandler("question", FAQ.get_faq, pass_args=True))
	dp.add_handler(CommandHandler("net", NET.get_net, pass_args=True))
	updates = bot.getUpdates()
	dp.add_error_handler(error)
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
    main()

