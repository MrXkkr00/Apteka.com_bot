from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contact_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="📱Контакт",
                                                      request_contact=True)
                                   ]
                               ])
