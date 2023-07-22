#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", "22070464", cast=int)
API_HASH = config("API_HASH", "65777c6927ee3bd024e4255a40d504e6")
BOT_TOKEN = config("BOT_TOKEN", "5794073832:AAEHEwnF3U9bfaASYYnxkKKJgtJpApFpjoU")
SESSION = config("SESSION", "BQBqu7r5AFsC4T0DUVQqQpSzHNo8FVPreLQfWF4ZXSLQSNppkvRYeR0QrRqiJpmvWNeheWVBKOXPpO-TAhHmDEsTsF9aBvCYub81bbRxKtk8KL6f3v1NXYa1G_lQM9ivw5rwHg1hMvyLQD2koUWAl4cz_glW0GQ67HarJOUPC_sahHEElujf8e4p_rQ_t8zDm3Nvgng8QZp48pa1qM3D1uZZ_GYx1lzor1KIXu0Q07Noj8ui3yZCiFHDZWDI6v75Kdz8DVmNkCUxnB_qkt3NgUBa88h6po_IpsJC-PegCAOJ3rWIH_q9JK8VbU-LD-KZMWVhiuD2vp_jdOpMjkJ1XzEoKUDaJQA")
FORCESUB = config("FORCESUB", "forcesuba")
AUTH = config("AUTH", "692116005", cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
