import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db import Database


TOKEN = "5366708049:AAGlHzxaYZ6uJdyngXTF8c5clxXwqBLIWm4"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

db = Database('database.db')

@dp.message_handler(commands='Start')
async def start(message: types.Message):
    if(not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Укажите ваше имя")
    else:
        markup = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Продолжить курс', callback_data='stat')
                                    ]
                                ])
        await bot.send_message(message.from_user.id, "Вы уже зарегистрированы!", reply_markup=markup)

@dp.callback_query_handler(text='stat')
async def start_button(call: types.CallbackQuery):
    await call.message.answer(text_modul, reply_markup=markup2)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == "Начать!":
            await bot.send_message(message.from_user.id, text_modul, reply_markup=markup2)
        else:
            if db.get_signup(message.from_user.id) == "setnickname":
                db.set_nickname(message.from_user.id, message.text)
                db.set_signup(message.from_user.id, "done")
                await bot.send_message(message.from_user.id, "Вы прошли регистрацию!", reply_markup=nav.mainMenu)
            else:
                await bot.send_message(message.from_user.id, "Что?")





text_modul = 'С другой стороны постоянный количественный рост и сфера нашей активности представляет'

markup2 = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Начать экзамен', callback_data='exam')
                                    ]
                                ])

@dp.callback_query_handler(text='exam')
async def start_button(call: types.CallbackQuery):
    await call.message.answer('Привет! Экзамен просто и тестовый, надеюсь ты справишься? Чтобы дать ответ пиши цифры 1 и 2')





if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
