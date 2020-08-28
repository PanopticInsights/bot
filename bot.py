# To install the tool for working with API telegrams, enter "pip install pytelegrambotapi"
# Telegram bot v. 0.0.1

import telebot

bot = telebot.TeleBot('1101310423:AAHp_G4V2YxNotfweYWXMwG8ogyFWaRT7GQ')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello, Tim')

bot.polling()
