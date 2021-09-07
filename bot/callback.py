from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import ASSISTANT_NAME as bn


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ HOW TO USE THIS BOT:

1.) First, add me to your group.
2.) Then promote me as admin and give all permissions except anonymous admin.
3.) Add @{bn} to your group.
4.) Turn on the voice chat first before start to stream video.
5.) Type /vstream (reply to video) to start streaming.
6.) Type /vstop to end the video streaming.

📝 **Note: stream & stop command can only be executed by group admin only!**

⚡ __Powered By Cyber System Database Server in Dubai__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🏡 Go Back", callback_data="cbstart")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"✨ **Hello there, I am a telegram group video streaming bot.**\n\n💭 **I was created to stream videos in group "
        f"video chats easily.**\n\n❔ **To find out how to use me, please press the help button below** 👇🏻",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "❔ HOW TO USE THIS BOT", callback_data="cbguide")
            ], [
                InlineKeyboardButton(
                    "🌐 Terms & Condition", callback_data="cbinfo")
            ], [
                InlineKeyboardButton(
                    "💬 Group", url="https://t.me/CyberSupportGroup"),
                InlineKeyboardButton(
                    "📣 Channel", url="https://t.me/CyberMusicProject")
            ], [
                InlineKeyboardButton(
                    "👩🏻‍💻 Developer", url="https://t.me/Badboyanim")
            ], [
                InlineKeyboardButton(
                    "📚 All Command List", callback_data="cblist")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🌐 **Bot information !**

🤖 __This bot was created to stream video in telegram group video chats using Cyber System Database Server in Dubai.__

💡 __Powered by PyTgcalls the Async client API for the Telegram Group Calls, and Pyrogram the telegram MTProto API 
Client Library and Framework in Pure Python for Users and Bots.__ 

👨🏻‍💻 __Thanks to the developers who participated in the development of this bot, the list of devs can be seen below:__

🤴 » [Arya Zakaria](https://github.com/aryazakaria01)
🤵🏻 » [Ihsan](https://github.com/UserLazy)
🤵🏻 » [Yoga Pranata](https://github.com/zYxDevs)
🤵🏻 » [Zero](https://github.com/Ryomen-Sukuna)

__This bot licensed under AGPL-3.0 License__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🏡 Go Back", callback_data="cbstart")
            ]]
        ),
        disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cblist"))
async def cblist(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""📚 All Command List:

❂ /vstream (reply to video or yt url) - To stream video
❂ /vstop - End the video streaming
❂ /song (song name) - Download song from YT
❂ /vsong (video name) - Download video from YT
❂ /lyric (song name) - Lyric scrapper

🎊 FUN CMD:

❂ /asupan - Check it by yourself
❂ /chika - Check it by yourself
❂ /wibu - Check it by yourself
❂ /truth - Check it by yourself
❂ /dare - Check it by yourself

🔰 EXTRA CMD:

❂ /tts (reply to text) - Text to speech
❂ /alive - Check bot alive status
❂ /ping - Check bot ping status
❂ /uptime - Check bot uptime status
❂ /sysinfo - Check bot system information

⚡ __Powered By Cyber System Database Server in Dubai__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🏡 Go Back", callback_data="cbstart")
            ]]
        ))


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
