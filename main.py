import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('5643787535:AAFxdHmSYvUXhlNRWg4kpbTlhtYBwRelzoU')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Открыть сайт🌐")
    btn2 = types.KeyboardButton("Найти товар🔎")
    markup.add(btn1, btn2)
    hello = f'Привет, {message.from_user.first_name}! Я тестовый бот. Что ты хочешь сделать?'
    bot.send_message(message.chat.id, hello, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Открыть сайт🌐':
        website(message)
    elif message.text == 'Найти товар🔎':
        msg_find = bot.send_message(message.chat.id, 'Что ищете?')
        bot.register_next_step_handler(msg_find, find)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю')

def find(message):
    bot.send_message(message.chat.id, 'Начинаю поиск')
    url = f'https://9v.ru/search?q={message.text}&lang=ru'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='product-preview__content')
    if quotes != []:
        for link in quotes:
            name = link.find('div', class_='product-preview__title').find('a').text
            links = 'https://9v.ru'+link.find('div', class_='product-preview__title').find('a').get('href')
            bot.send_message(message.chat.id, f'{name}\n{links}')
    else:
        bot.send_message(message.chat.id, 'К сожалению, ничего не найдено')
    

def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('🌐Открыть сайт🌐', url='https://9v.ru'))
    bot.send_message(message.chat.id,'Перейдите на сайт', reply_markup=markup)

bot.polling()