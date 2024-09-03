from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bosh_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔍 Поиск лекарств"),
        ],
        [
            KeyboardButton(text="Как пользоваться❓"),
        ],
        [
            KeyboardButton(text="📝 Оставить отзыв"),
            KeyboardButton(text="Информация 📖")
        ],
    ],resize_keyboard=True
)

information = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ℹ️ О нас"),
        ],
        [
            KeyboardButton(text="📞 Контакты"),
        ],

        [
            KeyboardButton(text="🤖Программист телеграмм-ботов от 50$ до 200$"),
        ],
    ],resize_keyboard=True
)

qayta_izlash_IN = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="📋Разместить заказ", callback_data="📋Разместить заказ"),
    ],
    [
        InlineKeyboardButton(text="🔍Поиск снова", callback_data="🔍Поиск снова"),
    ],
    [
        InlineKeyboardButton(text="Главное меню", callback_data="Главное меню"),
    ],

])

qayta_izlash = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="📋Разместить заказ"),
    ],
    [
        KeyboardButton(text="🔍Поиск снова"),
    ],
    [
        KeyboardButton(text="Главное меню"),
    ],

], resize_keyboard=True
)

bosh_menu_IN = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🔍 Поиск лекарств", callback_data="🔍 Поиск лекарств"),
    ],
    [
        InlineKeyboardButton(text="Как пользоваться❓", callback_data="Как пользоваться❓"),
    ],
    [
        InlineKeyboardButton(text="📝 Оставить отзыв", callback_data="📝 Оставить отзыв"),
        InlineKeyboardButton(text="Информация 📖", callback_data="Информация 📖"),
    ],

])