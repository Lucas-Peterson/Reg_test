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

count = 0

@dp.message_handler(commands='Start')
async def start(message: types.Message):
    if(not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Укажите ваше имя")
    else:
        markup = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Продолжить курс', callback_data='sequel')
                                    ]
                                ])
        await bot.send_message(message.from_user.id, "Вы уже зарегистрированы!", reply_markup=markup)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message. chat. type == 'private':
        if message. text == "Начать!":
            await bot.send_message(message.from_user.id, text_modul)
        else:
            if db.get_signup(message.from_user.id) == "setnickname":
                db.set_nickname(message.from_user.id, message.text)
                db.set_signup(message.from_user.id, "done")
                await bot.send_message(message.from_user.id, "Вы прошли регистрацию!", reply_markup=nav.mainMenu)
            else:
                await bot.send_message(message.from_user.id, "Что?")


text_modul = 'Прямо большой курс, текст и ещё раз текст'

markup_1 = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Начать экзамен', callback_data='exam')
                                    ]
                                ])

markup_2 = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Да!', callback_data='Start_exam')
                                    ]
                                ])

markup_3 = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Правильный ответ', callback_data='True'),
                                        InlineKeyboardButton(text='Неправильный ответ', callback_data='False')
                                    ]
                                ])

markup_check = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Да!', callback_data='Check')
                                    ]
                                ])


@dp.callback_query_handler(text='exam')
async def exam(call: types.CallbackQuery):
    await call.message.answer('Привет! Экзамен простой и тестовый, надеюсь ты справишься? Ты готов?', reply_markup=markup_2, )

@dp.callback_query_handler(text='True')
async def Truech(call: types.CallbackQuery):
    await call.message.answer('Правильно!')


@dp.callback_query_handler(text='False')
async def false(call: types.CallbackQuery):
    await call.message.answer('Неправильно!')

@dp.callback_query_handler(text='Start_exam')
async def start_exam(call: types.CallbackQuery):
    await call.message.answer('Вопрос 1', reply_markup= markup_3)

@dp.callback_query_handler(text='sequel')
async def seqel(call: types.CallbackQuery):
    await call.message.answer(text_modul, reply_markup=markup_1)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)