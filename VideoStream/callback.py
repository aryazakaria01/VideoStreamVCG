# Copyright (C) 2021 By VideoStreamVCG

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import Cyber


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ HOW TO USE THIS BOT:

1.) First, add me to your group.
2.) Then promote me as admin and give all permissions except anonymous admin.
3.) Add @{Cyber.ASSISTANT_NAME } to your group.
4.) Turn on the voice chat first before start to stream video.
5.) Type /vplay (reply to video) to start streaming.
6.) Type /vstop to end the video streaming.

📝 **Note: stream & stop command can only be executed by group admin only!**

⚡ __Maintained by Cyber Team__""",
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
        f"Video chats easily.**\n\n❔ **To find out how to use me, please press the help button below** 👇🏻",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "➕ Add me to your Group ➕", url=f"https://t.me/{Cyber.BOT_USERNAME}?startgroup=true")
            ], [
                InlineKeyboardButton(
                    "❔ HOW TO USE THIS BOT", callback_data="cbguide")
            ], [
                InlineKeyboardButton(
                    "🌐 Terms & Condition", callback_data="cbinfo")
            ], [
                InlineKeyboardButton(
                    "💬 Group", url=f"https://t.me/{Cyber.GROUP_NAME}"),
                InlineKeyboardButton(
                    "📣 Channel", url=f"https://t.me/{Cyber.CHANNEL_NAME}")
            ], [
                InlineKeyboardButton(
                    "🧙🏻‍♂️ Owner", url=f"https://t.me/{Cyber.OWNER_NAME}")
            ], [
                InlineKeyboardButton(
                    "📚 All Command List", callback_data="cblist")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🌐 **Bot information !**

🤖 __This bot was created to stream video in telegram group video chats using several methods from WebRTC and CyberUPH-8.__

💡 __Powered by PyTgcalls the Async client API for the Telegram Group Calls, and Pyrogram the telegram MTProto API 

Client Library and Framework in Pure Python for Users and Bots.__

👨🏻‍💻 __Thanks to the developers who participated in the development of this bot, the list of devs can be seen below:__

👩🏻‍✈️ » [Arya Zakaria](https://github.com/aryazakaria01)
🤵🏻 » [Sammy-XD](https://github.com/Sammy-XD)
🤵🏻 » [Zxce3](https://github.com/Zxce3)
🤵🏻 » [Tofik Denianto](https://github.com/tofikdn)
🤵🏻 » [Shohih Abdul](https://github.com/DoellBarr)

__This bot licensed under GNU-GPL 3.0 License__""",
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

➛ /vplay (reply to video or yt/live url) - to stream video
➛ /vstop - stop the video streaming
➛ /song (song name) - download song from YT
➛ /vsong (video name) - download video from YT
➛ /lyric (song name) - lyric scrapper
➛ /vjoin - invite assistant join to your group
➛ /vleave - order assistant leave from your group

🎊 FUN CMD:

➛ /asupan - check it by yourself
➛ /chika - check it by yourself
➛ /wibu - check it by yourself
➛ /truth - check it by yourself
➛ /dare - check it by yourself

🔰 EXTRA CMD:

➛ /tts (reply to text) - text to speech
➛ /alive - check bot alive status
➛ /ping - check bot ping status
➛ /uptime - check bot uptime status
➛ /sysinfo - check bot system information

💡 SUDO ONLY:

➛ /rmd - remove all downloaded files
➛ /rmw - remove all downloaded raw files
➛ /leaveall - order assistant leave from all group

⚡ __Maintained by Cyber Team__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🏡 Go Back", callback_data="cbstart")
            ]]
        ))


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
