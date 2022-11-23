#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", " 13673662", cast=int)
API_HASH = config("API_HASH", " 90a8ca652259ec84f9ab4afdc7e3846e")
BOT_TOKEN = config("BOT_TOKEN", " 5774243125:AAH3Pals4yFld2ioLAVv3OdbKQhnTWmWYFQ")
SESSION = config("SESSION", " BQCdLmcMey4wMkHB9pCcSkO90fRDXvOejlr-CCmfcxpqLrrzb5VketzevI_LE3zESRC_XsmWj_0kJ4sE_LmEfgJXdeVdku1t-Au8aNDq-zYU75N9fnIiwszIKz2YocIEOEs2kutaG2lD9rbyninVtBwgBR9kW6eCSYaMeeaIt6GO4ci30mgdmJY39I4_TdFf9eBBJWsNMxbDG4FDj1qe1UGlM4eVFLIVkQSRQwdxR9ITNa__xf5AcgAmi_BJftIynXxIxfkrC8ryYlQzRpPsjxtvN4DFxDspxZa1G5oKaMIbZTL_kGcIGuaHq5DQjamU17MxzPXz8SOxX7DSBYKJ6aU0AAAAATKhhykA")
FORCESUB = config("FORCESUB", " savecontentar01")
AUTH = config("AUTH", " 5144413993", cast=int)

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
