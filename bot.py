import config

import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

source_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
source_markup_btn1 = types.KeyboardButton('Ongoing')
source_markup_btn2 = types.KeyboardButton('Upcoming')
source_markup.add(source_markup_btn1, source_markup_btn2)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, "Хаю хай")



@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)
