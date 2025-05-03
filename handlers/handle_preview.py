from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def handle_preview(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🌐 Open HTML Page", url="https://yevhenii1313ilin.github.io/openpulse-preview")],
        [InlineKeyboardButton(text="📄 Download PDF", url="https://yevhenii1313ilin.github.io/openpulse-preview/OpenPulse_5Slides_Presentation.pdf")],
        [InlineKeyboardButton(text="📦 Download ZIP", url="https://yevhenii1313ilin.github.io/openpulse-preview/OpenPulse_FullPackage.zip")]
    ])

    text = (
        "🧠 *OpenPulse – Developer Preview*\n"
        "The rhythmic open-weight model for emotional, modular, and collaborative AI.\n\n"
        "Explore the vision, download the full package, or join the rhythm."
    )
    await message.answer(text, reply_markup=keyboard, parse_mode="Markdown")
