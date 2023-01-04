from aiogram.utils import executor
from create_bot import dp


async def on_startup(_):
    print("Bot is onlayn")

import client, admin, other

client.register_handlers_client(dp)
other.register_handlers_client(dp)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)