import requests
import telebot
from bs4 import BeautifulSoup
bot = telebot.TeleBot('5643787535:AAFxdHmSYvUXhlNRWg4kpbTlhtYBwRelzoU')


def find_text(message):
    bot.send_message(message.chat.id, 'Начинаю поиск')
    url = f'https://9v.ru/search?q={message.text}&lang=ru'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='product-preview__content')
    return quotes