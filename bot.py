import telebot
import time
import pyshorteners
import os

bot = telebot.TeleBot(token=os.getenv('TG_BOT_TOKEN'))

@bot.message_handler(commands=['start'])
def text(message):
    chatid = message.chat.id
    bot.send_photo(chatid, open('1566206027.png','rb'))

        bot.polling()

