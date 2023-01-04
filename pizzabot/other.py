from aiogram import types, Dispatcher
from create_bot import dp
import string, json


#@dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('combined.json')))) != set():
        await message.reply('Не треба лаятись, ЗАБОРОНЕНО!')
        await message.delete()

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(echo_send)
