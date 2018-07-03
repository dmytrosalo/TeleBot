import config

import telebot
import markups as m
import dota2

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, "Хаю хай")
    msg = bot.send_message(message.chat.id,'Че ты хош?', reply_markup=m.source_markup)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if text == 'ongoing':
        bot.send_message(chat_id, dota2.getTitlesFromAll(text))
    elif text == 'upcoming':
        bot.send_message(chat_id, dota2.getTitlesFromAll(text))


if __name__ == '__main__':
    bot.polling(none_stop=True)
