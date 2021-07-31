import telebot
import time
import pyshorteners
import os

bot = telebot.TeleBot(token=os.getenv('TG_BOT_TOKEN'))

@bot.message_handler(commands=['list'])
def send_welcome(message):
    bot.reply_to(message, '''List Yang Kami Jual Disini
===========
1. YouTube Premium 4 Bulan = 3k
2. YouTube Premium 1 Bulan = 1k
3. Nokos Telegram USA = 1.200
4. Nokos Telegram ID = 1.700
5. Nokos WhatsApp = 1k
===========
Silahkan dipilih, dan ketikkan apa yang ingin anda beli, admin akan membalas nya secepat mungkin''')

@bot.message_handler(commands=['tesf'])
def text(message):
    chatid = message.chat.id
    bot.send_photo(chatid, open('1566206027.png','rb'))


bot.polling()

