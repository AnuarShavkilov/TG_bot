import telebot
from telebot import types
from pars import find_text
# from resistor import ring_count, first_ring, second_ring, third_ring, fourth_ring, last_ring

bot = telebot.TeleBot('5643787535:AAFxdHmSYvUXhlNRWg4kpbTlhtYBwRelzoU')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Открыть сайт🌐")
    btn2 = types.KeyboardButton("Найти товар🔎")
    btn3 = types.KeyboardButton("Калькулятор резисторов")
    markup.add(btn1, btn2, btn3)
    hello = f'Привет, {message.from_user.first_name}! Я тестовый бот. Что ты хочешь сделать?'
    bot.send_message(message.chat.id, hello, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Открыть сайт🌐':
        website(message)
        ozon_site(message)
        wild_site(message)
        ym_site(message)
    elif message.text == 'Найти товар🔎':
        msg_find = bot.send_message(message.chat.id, 'Что ищете?')
        bot.register_next_step_handler(msg_find, find)
    elif message.text == 'Калькулятор резисторов':
        msg_calc = bot.send_message(message.chat.id, 'Сколько колец на резисторе')
        # bot.register_next_step_handler(msg_calc, resis_calc)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю')

def find(message):
    result_pars = find_text(message)

    if result_pars != []:
        for link in result_pars:
            name = link.find('div', class_='product-preview__title').find('a').text
            links = 'https://9v.ru'+link.find('div', class_='product-preview__title').find('a').get('href')
            bot.send_message(message.chat.id, f'{name}\n{links}')
    else:
        bot.send_message(message.chat.id, 'К сожалению, ничего не найдено')

    bot.send_message(message.chat.id, 'Если Вы не нашли что искали')
    website(message)
    bot.send_message(message.chat.id, 'Или позвоните нам по номеру 📲\n+7(843)259-19-16')

def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('🌐Открыть сайт🌐', url='https://9v.ru'))
    bot.send_message(message.chat.id,'Перейдите на сайт', reply_markup=markup)

def ozon_site(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('OZON', url='https://www.ozon.ru/seller/radio-tochka-21003'))
    bot.send_message(message.chat.id,'⬇ Магазин ⬇', reply_markup=markup)

def wild_site(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Wildberries', url='https://www.wildberries.ru/brands/9vru'))
    bot.send_message(message.chat.id,'⬇ Магазин ⬇', reply_markup=markup)

def ym_site(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Яндекс.Маркет', url='https://market.yandex.ru/business--radio-tochka-rf-9v-ru/932565'))
    bot.send_message(message.chat.id,'⬇ Магазин ⬇', reply_markup=markup)

# def resis_calc(message):
#     colors = ['коричневый', 'красный', 'оранжевый', 'желтый', 'зеленый',
#               'голубой', 'фиолетовый', 'серый', 'белый', 'черный',
#               'золотистый', 'серебристый']
#     n = message.text

bot.polling()