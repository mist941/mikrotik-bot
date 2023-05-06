import os
from dotenv import load_dotenv, find_dotenv
import telebot
from telebot import types
from messages import prepared_messages

load_dotenv(find_dotenv())

bot_token = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, prepared_messages["start_message"])


bot.polling(none_stop=True, interval=0)
