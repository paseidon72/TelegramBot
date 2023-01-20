import telebot

bot = telebot.TeleBot('hdijwheriu3274*LAJA*98237659efhiu3h4')
users = set()

@bot.message_handler(func=lambda message: not message.from_user.is_bot)
def on_message(message):
    print(message)
    bot.send_message(message.from_user.id, 'text')

    for user in users:
        if user != message.from_user.id:
            bot.send_message(user, message.text)
    users.add(message.from_user.id)


bot.polling(none_stop=True)