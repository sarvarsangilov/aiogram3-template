import asyncio

from handlers import router
from loader import dp, bot
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


import utils


async def on_startup():
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(bot)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(bot)


async def main():

    dp.include_router(router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main(), debug=True)
