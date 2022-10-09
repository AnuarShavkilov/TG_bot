import telebot
bot = telebot.TeleBot('5643787535:AAFxdHmSYvUXhlNRWg4kpbTlhtYBwRelzoU')

@bot.message_handler(commands=['start'])
def start(message):
    name = f'Dattebayo, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, name, parse_mode='html')

bot.polling(none_stop=True)
