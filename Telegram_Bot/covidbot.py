import telebot
import COVID19Py

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>Привет {message.from_user.first_namee}!</b>\nВведите страну"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')



bot.polling(none_stop=True)