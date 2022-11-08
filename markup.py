from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, types

TOKEN = "5366708049:AAGlHzxaYZ6uJdyngXTF8c5clxXwqBLIWm4"

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

btnStart = KeyboardButton('Начать!')

mainMenu = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu.add(btnStart)

markup_course = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Начать курс', callback_data='course')
                                    ]
                                ])

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


text_modul = 'Прямо большой курс, текст и ещё раз текст'