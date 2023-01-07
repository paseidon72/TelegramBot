from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os



bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(message.text) #просто отвечает повтором
    await message.reply(message.text) #отвечает повтором с указанием имени кто писал
    await bot.send_message(message.from_user.id, message.text) #отвечает из группы в личку


executor.start_polling(dp, skip_updates=True)