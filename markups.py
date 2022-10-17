from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnStart = KeyboardButton('Начать!')

mainMenu = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu.add(btnStart)


markup = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Продолжить курс', callback_data='stat')
                                    ]
                                ])


@dp.callback_query_handler(text='stat')
async def start_button(call: types.CallbackQuery):
    await call.message.answer(text_modul, reply_markup=markup2)



markup2 = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Начать экзамен', callback_data='exam')
                                    ]
                                ])


@dp.callback_query_handler(text='exam')
async def exam(call: types.CallbackQuery):
    await call.message.answer('Привет! Экзамен просто и тестовый, надеюсь ты справишься? Ты готов?')


