#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", "17718356", cast=int)
API_HASH = config("API_HASH", "fe2dec8e960bf8dcb4e4820d81fe7d46")
BOT_TOKEN = config("BOT_TOKEN", "5644454947:AAHaMbdZUQgqwRrO3aZszDQ8o9AT8a2pF6E")
SESSION = config("SESSION", "BQCf3ZJRphYVxJOGlvDIY29BPwTKR9RKYxJgJX_gNqDLZPA80z_9R1qOuA1aTbDxU7RomZXwDh4_6SC6fux7PGn_mLsVjX-m6xuV3uXPK4r4XRNVwvpv9O8RnDyMMWr8UsXX8dO5T3MgepIPa0RZCQRQ94KccoobX_VEjv2hzgeQ3t-skRwZZLTTJpa-NFN3_mrfLNcB8IA7HTMNi4nlzT5Ljbom-dtlHbQoM9Bau3ozyW16DgCYhrss3DwERrWoi022YK_0iOqpvLn0mBEwr3Eox9oinZHbLIk792XOyMX5lkh9526C1JIj-SdayRkpvtRzXNYpFoFWAMkqWTjxUHk0AAAAAVre2SwA")
FORCESUB = config("FORCESUB", "arbackup1")
AUTH = config("AUTH", "5819521324", cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

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
