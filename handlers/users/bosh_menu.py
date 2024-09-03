from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, InputFile, CallbackQuery

from handlers.users.search_menu import Searchstate
from keyboards.default.menu import bosh_menu, information
from loader import dp, bot


class Comment_about(StatesGroup):
    comment = State()





@dp.message_handler(text="Информация 📖")
async def bot_start2(message: types.Message):
    await message.answer(f"information", reply_markup=information)


@dp.callback_query_handler(text="Информация 📖")
async def buy_cour3424ses(call: CallbackQuery):
    await call.message.answer(f"information", reply_markup=information)
    await call.message.delete()


@dp.message_handler(text="🤖Программист телеграмм-ботов от 50$ до 200$")
async def rekalma(message: types.Message):
    # await bot.send_photo(chat_id=message.from_user.id, photo="./data/bot.jpg")
    photo = InputFile('./data/bot.jpg')
    await message.answer_photo(photo, caption=
    f"Сервис создания ботов в Telegram."
    f"\nБоты, которые предоставляют пользователям какие-то услуги."
    f"\nИ очень низкая цена, потому что я не какая-то ИТ-фирма или компания."
    f"\nЯ простой программист, у которого даже нет офиса, и это избавит вас от лишних расходов."
    f"\nЦена услуги оговаривается в зависимости от сложности бота, от 20S до 100S."
    f"\nTelegram-боты всех типов:"
    f"\nИнтернет-журнал;"
    f"\nРабота с информацией с сайта;"
    f"\nБоты-регистраторы"
    f"\nБоты для каналов;"
    f"\nБоты для групп;"
    f"\nОсобенности: удобная админка, автоплатежные системы, высокая скорость."
    f"Телеграм: +998993321038", reply_markup=bosh_menu)


@dp.message_handler(text="ℹ️ О нас")
async def bot_start2_1(message: types.Message):
    await message.answer(f"Добро пожаловать в онлайн аптека мы оказываем услуги доставки "
                         f"лекарства производство Россия Украина Европа Индия, если вы не можете найти "
                         f"нужную лекарства обращайте нам.", reply_markup=bosh_menu)


@dp.message_handler(text="📞 Контакты")
async def bot_start3_1(message: types.Message):
    await message.answer(f"+192927193374", reply_markup=bosh_menu)


@dp.message_handler(text="📝 Оставить отзыв")
async def bot_star4t(message: types.Message):
    await message.answer(f"Оставляйте свои комментарии и предложения!", reply_markup=ReplyKeyboardRemove())
    await Comment_about.comment.set()


@dp.callback_query_handler(text="📝 Оставить отзыв")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"Оставляйте свои комментарии и предложения!", reply_markup=ReplyKeyboardRemove())
    await call.message.delete()
    await Comment_about.comment.set()


@dp.message_handler(state=Comment_about.comment)
async def bot_start5(message: types.Message, state: FSMContext):
    await message.answer(f"Спасибо большое, нам очень важно ваше мнение!", reply_markup=bosh_menu)
    await bot.send_message(chat_id=984568970, text=f"@{message.from_user.username}\n{message.text}")
    await state.finish()












