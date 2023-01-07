import requests
import random
import telebot
from bs4 import BeautifulSoup as b

url = 'https://etnosvit.com/uk/anekdoty_uk.html'
API_KEY = ""
def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anecdots = soup.find_all('div', class_='sue-panel-content sue-content-wrap')
    return [c.text for c in anecdots]

list_of_jokes = parser(url)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['начать'])

def hell(message):
    bot.send_message(message.chat.id, 'Дорого дня щоб отримати анекдот пишіть будь яку цифру: ')

@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'пишіть цифру, анекдоти лише за цифрами:')

bot.polling()

