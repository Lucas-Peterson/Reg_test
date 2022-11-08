import logging
from aiogram import Bot, Dispatcher, executor, types
import markup as nav
from markup import text_modul
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
        await bot.send_message(message.from_user.id, "Вы уже зарегистрированы!", reply_markup=nav.markup_course)

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


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)