#Aiogramni dasturimizga import qilib olamiz
import logging
from aiogram import Bot, Dispatcher, executor, types

#o'tgan videodagi hashlibni ham import qilamiz xabarni xeshlash uchun
import hashlib


#telegramda bot yaratib undan api key ni shu yerga qo'yamiz
API_TOKEN = "BOT TOKEN"

#bot bilan dasturimizni ulaymiz
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)   #bot degan o'zgaruvchi yaratib uni yuqoridagi api tokenga ulaymiz
dp = Dispatcher(bot)  #bot uchun dispatcher yaratib olamiz



@dp.message_handler(commands=['start']) # start buyrug'i boslganda qandaydir ishni bajarishi uchun
async def start(message: types.Message):  #start uchun funksiya yaratamiz va unga message parametrlarini beramiz
    await message.answer("Botga so'z yuboring va u sizga so'zni MD5 xesh ko'rinishida yuboradi")
    # start bosilganda shu xabarni yubor degani 


@dp.message_handler()
async def md5(message: types.Message):  #yana bitta funksiya yaratamiz va u zabarnini xesh ko'rinishiga o'tkazib userga yuborishi kerak

    await message.reply("MD5 Xesh parolingiz : " + (hashlib.md5(message.text.encode())).hexdigest())

    #userdan kelgan xabar textini enkod qilib md5 ga o'tkaz va ushbu so'zga qo'shib userga qaytarib yubor


#Botni polling qil ya'ni botni ishlat bu haqida mukammal bilishingiz shart emas
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

