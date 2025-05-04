from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.message(commands=["preview"])
async def handle_preview(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🌐 Open HTML Page", url="https://yevhenii1313ilin.github.io/openpulse-preview")],
        [InlineKeyboardButton(text="📄 Download PDF (EN)", url="https://yevhenii1313ilin.github.io/openpulse-preview/OpenPulse_English_Preview.pdf")],
        [InlineKeyboardButton(text="📦 Download ZIP Package", url="https://yevhenii1313ilin.github.io/openpulse-preview/OpenPulse_FullPackage.zip")]
    ])
    text = (
        "🧠 *OpenPulse – Developer Preview*\n"
        "The rhythmic open-weight model for emotional, modular, and collaborative AI.\n\n"
        "Explore the vision, download the full package, or join the pulse."
    )
    await message.answer(text, reply_markup=keyboard, parse_mode="Markdown")
