# ===========
# running bot
# ===========

from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from VideoStream.videoplayer import app


bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="VideoStream"),
)

bot.start()
print("[INFO]: STARTING BOT CLIENT")
app.start()
print("[INFO]: STARTING USERBOT CLIENT")
idle()
print("[INFO]: STOPPING BOT")
