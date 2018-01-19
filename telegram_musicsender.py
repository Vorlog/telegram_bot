import random
import telebot
import os

from common import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def text_handler(message):
    if 'музыку' in str(message.text).lower():
        random_mp3 = open(BASE_DIR + random.choice(os.listdir(BASE_DIR)), 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, random_mp3)
        random_mp3.close()
        bot.send_message(message.from_user.id, 'Понравилась?')
    elif 'да' in str(message.text).lower():
        bot.send_message(message.chat.id, 'Тогда заказывай еще!')
    else:
        bot.send_message(message.chat.id, 'WTF?')

bot.polling(none_stop=True, interval=0)


