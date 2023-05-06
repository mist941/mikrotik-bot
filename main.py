import os
import re
import telebot
from dotenv import load_dotenv, find_dotenv
from telebot import types
from mikrotik_actions import connection
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv(find_dotenv())

bot_token = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        'Write username, IP and password of your mikrotik\nFor example "admin 192.168.88.1 password"'
    )


@bot.message_handler(content_types=['text'])
def send_text(message):
    if re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", message.text):
        ssh_params = message.text.split(" ")
        ssh_user = ssh_params[0]
        ssh_ip = ssh_params[1]
        ssh_password = ssh_params[2]
        connection_message = connection(ssh_user=ssh_user, ssh_ip=ssh_ip, ssh_password=ssh_password)

        if connection_message == 'Failed connection':
            bot.send_message(message.chat.id, connection_message)
        else:
            update = InlineKeyboardButton(text='Update Router OS', callback_data='update_router')
            keyboard = [[update]]
            bot.send_message(
                chat_id=message.chat.id,
                text=connection_message + ". What can I help you",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

    else:
        bot.send_message(message.chat.id, 'I do not understand you')


def update_router(message):
    bot.send_message(message.chat.id, 'Update')


handler = CallbackQueryHandler(update_router, pattern='^update_router$')

bot.polling(none_stop=True, interval=0)
