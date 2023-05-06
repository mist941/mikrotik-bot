import os
import re
import telebot
from dotenv import load_dotenv, find_dotenv
from telebot import types
from messages import prepared_messages
from mikrotik_actions import connection

load_dotenv(find_dotenv())

bot_token = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, prepared_messages["start_message"])


@bot.message_handler(content_types=['text'])
def send_text(message):
    if re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", message.text):
        ssh_params = message.text.split(" ")
        ssh_user = ssh_params[0]
        ssh_ip = ssh_params[1]
        ssh_password = ssh_params[2]
        connection_message = connection(ssh_user=ssh_user, ssh_ip=ssh_ip, ssh_password=ssh_password)
        print(connection_message)
    else:
        bot.send_message(message.chat.id, prepared_messages["wrong_question"])


bot.polling(none_stop=True, interval=0)
