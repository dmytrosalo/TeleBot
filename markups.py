from telebot import types

source_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
source_markup_btn1 = types.KeyboardButton('Ongoing')
source_markup_btn2 = types.KeyboardButton('Upcoming')
source_markup_btn3 = types.KeyboardButton('TI8')
source_markup.add(source_markup_btn1, source_markup_btn2, source_markup_btn3)
