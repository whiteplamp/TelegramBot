import logging
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

logging.basicConfig(level = logging.INFO)

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)

@dp.message_handler
async def start(message:types.Message):
  await message.reply("Hello, world!")

@dp.message_handler()
async def repeat(message:types.Message):
  await message.answer(message.text)


if __name__ == '__main__':
  executor.start_polling(dp, skip_updates = True)
