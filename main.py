from email import message
import telebot
from telebot import types

bot = telebot.TeleBot('5643787535:AAFxdHmSYvUXhlNRWg4kpbTlhtYBwRelzoU')

@bot.message_handler(commands=['start'])
def start(message):
    name = f'Dattebayo, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, name, parse_mode='html')

# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == 'Привет':
#         bot.send_message(message.chat.id, 'Салам молекулам')
#     elif message.text == 'Котак':
#         bot.send_message(message.chat.id, f'Котак - {message.from_user.first_name}')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id,'Крутое фото')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Открыть сайт', url='https://9v.ru'))
    bot.send_message(message.chat.id,'Перейдите на сайт', reply_markup=markup)

@bot.message_handler(commands=['help'])
def butt(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('/website')
    start = types.KeyboardButton('/start')
    markup.add(website, start)
    bot.send_message(message.chat.id,'Помощь', reply_markup=markup)


bot.polling(none_stop=True)
