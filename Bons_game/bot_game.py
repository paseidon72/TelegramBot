from aiogram import Bot, Dispatcher, executor, types
from asyncio import sleep


bot = Bot('hdijwheriu3274*LAJA*98237659efhiu3h4')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def on_message(message: types.Message):
    await bot.send_message(message.from_user.id, f"Hello! {message.from_user.username} Start game?")
    await sleep(1)

    bot_data = await bot.send_dice(message.from_user.id)
    bot_data = bot_data['dice']['value']
    await sleep(5)

    user_data = await bot.send_dice(message.from_user.id)
    user_data = user_data['dice']['value']
    await sleep(5)

    if bot_data > user_data:
        await bot.send_message(message.from_user.id, "Ooo Your Lost")
    elif bot_data < user_data:
        await bot.send_message(message.from_user.id, "Yes Your Won")
    else:
        await bot.send_message(message.from_user.id, "So/So")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
