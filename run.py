import asyncio, logging, sys
from aiogram import Dispatcher


from app.hls import router as hls_router
from app.statehls import router as statehls_router
from bot import bot, translator

dp = Dispatcher()
translator.register(dp)

async def main():
    dp.include_router(hls_router)
    dp.include_router(statehls_router)

    await dp.start_polling(bot)

        
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot disabled.")
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        