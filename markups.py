from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnStart = KeyboardButton('Начать!')

mainMenu = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu.add(btnStart)
