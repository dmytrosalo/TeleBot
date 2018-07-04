import urllib.request

import telebot
import markups as m
import dota2

import config


bot = telebot.TeleBot(config.token)
CHANNEL_NAME = '@kkapustka'


def send_img_url_message(chat_id, img_url):
    img = urllib.request.urlopen(img_url)
    bot.send_photo(chat_id, img)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    chat_id = message.chat.id
    # filehandle = urllib.request.urlopen(img_url)
    # bot.send_photo(chat_id, filehandle)
    msg = bot.send_message(chat_id,'Че ты хош?', reply_markup=m.source_markup)




@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    chat_id = message.chat.id
    text = message.text.lower()
    # bot.send_message(CHANNEL_NAME, text)
    if text == 'ongoing':
        bot.send_message(chat_id, dota2.getMatchesData(text))
    elif text == 'upcoming':
        bot.send_message(chat_id, dota2.getMatchesData(text))
    elif text == 'ti8':
        ti_teams = dota2.getTIData()
        print(ti_teams)
        for team in ti_teams:
            print(team)
            bot.send_message(chat_id, team["name"])
            send_img_url_message(chat_id, team['logo_url'] )

if __name__ == '__main__':
    bot.polling(none_stop=True)
