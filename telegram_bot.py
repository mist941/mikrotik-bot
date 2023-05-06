import os
from dotenv import load_dotenv
import telebot

load_dotenv()

bot_token = os.getenv("VARIABLE_NAME")
bot = telebot.TeleBot(bot_token)

bot.polling(none_stop=True, interval=0)