import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from handle_preview import router as preview_router

# 🔐 Your bot token here
BOT_TOKEN = "your_bot_token_here"

# Init bot & dispatcher
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.MARKDOWN)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(commands=["start"])
async def handle_start(message: types.Message):
    await message.answer("👋 Hello! I'm your PlayAI companion. Use /preview to see OpenPulse.")

# Register routers
dp.include_router(preview_router)

# Run bot
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())