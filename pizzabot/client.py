from aiogram import types, Dispatcher
from create_bot import dp, bot
from kb_client import kb_client
from aiogram.types import ReplyKeyboardRemove


#@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Смачного!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Спілкування з Адмін-Бот через ЛС, перейдіть за посиланням:\nhttps://t.me/loadmodel_bot')

#@dp.message_handler(commands=['Розклад_роботи'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт з 9:00 до 20:00\nСб-Нд з 10:00 до 23:00')

#@dp.message_handler(commands=['Розташування'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'вул. Вкусняшка 22', reply_markup=ReplyKeyboardRemove())

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Розклад'])
    dp.register_message_handler(pizza_place_command, commands=['Розташування'])
