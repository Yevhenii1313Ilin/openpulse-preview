import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from handlers.handle_preview import router as preview_router

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.MARKDOWN)
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(preview_router)

@dp.message(commands=["start"])
async def start(message: types.Message):
    await message.answer("👋 Welcome to OpenPulse Preview. Type /preview to begin.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
