# Copyright (C) 2021 By VideoStreamVCG

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import Cyber


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ā HOW TO USE THIS BOT:

1.) First, add me to your group.
2.) Then promote me as admin and give all permissions except anonymous admin.
3.) Add @{Cyber.ASSISTANT_NAME } to your group.
4.) Turn on the voice chat first before start to stream video.
5.) Type /vplay (reply to video) to start streaming.
6.) Type /vstop to end the video streaming.

š **Note: stream & stop command can only be executed by group admin only!**

ā” __Maintained by Cyber Team__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "š” Go Back", callback_data="cbstart")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"āØ **Hello there, I am a telegram group video streaming bot.**\n\nš­ **I was created to stream videos in group "
        f"Video chats easily.**\n\nā **To find out how to use me, please press the help button below** šš»",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "ā Add me to your Group ā", url=f"https://t.me/{Cyber.BOT_USERNAME}?startgroup=true")
            ], [
                InlineKeyboardButton(
                    "ā HOW TO USE THIS BOT", callback_data="cbguide")
            ], [
                InlineKeyboardButton(
                    "š Terms & Condition", callback_data="cbinfo")
            ], [
                InlineKeyboardButton(
                    "š¬ Group", url=f"https://t.me/{Cyber.GROUP_NAME}"),
                InlineKeyboardButton(
                    "š£ Channel", url=f"https://t.me/{Cyber.CHANNEL_NAME}")
            ], [
                InlineKeyboardButton(
                    "š§š»āāļø Owner", url=f"https://t.me/{Cyber.OWNER_NAME}")
            ], [
                InlineKeyboardButton(
                    "š All Command List", callback_data="cblist")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""š **Bot information !**

š¤ __This bot was created to stream video in telegram group video chats using several methods from WebRTC and CyberUPH-8.__

š” __Powered by PyTgcalls the Async client API for the Telegram Group Calls, and Pyrogram the telegram MTProto API 

Client Library and Framework in Pure Python for Users and Bots.__

šØš»āš» __Thanks to the developers who participated in the development of this bot, the list of devs can be seen below:__

š©š»āāļø Ā» [Arya Zakaria](https://github.com/aryazakaria01)
š¤µš» Ā» [Sammy-XD](https://github.com/Sammy-XD)
š¤µš» Ā» [Zxce3](https://github.com/Zxce3)
š¤µš» Ā» [Tofik Denianto](https://github.com/tofikdn)
š¤µš» Ā» [Shohih Abdul](https://github.com/DoellBarr)

__This bot licensed under GNU-GPL 3.0 License__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "š” Go Back", callback_data="cbstart")
            ]]
        ),
        disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cblist"))
async def cblist(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""š All Command List:

ā /vplay (reply to video or yt/live url) - to stream video
ā /vstop - stop the video streaming
ā /song (song name) - download song from YT
ā /vsong (video name) - download video from YT
ā /lyric (song name) - lyric scrapper
ā /vjoin - invite assistant join to your group
ā /vleave - order assistant leave from your group

š FUN CMD:

ā /asupan - check it by yourself
ā /chika - check it by yourself
ā /wibu - check it by yourself
ā /truth - check it by yourself
ā /dare - check it by yourself

š° EXTRA CMD:

ā /tts (reply to text) - text to speech
ā /alive - check bot alive status
ā /ping - check bot ping status
ā /uptime - check bot uptime status
ā /sysinfo - check bot system information

š” SUDO ONLY:

ā /rmd - remove all downloaded files
ā /rmw - remove all downloaded raw files
ā /leaveall - order assistant leave from all group

ā” __Maintained by Cyber Team__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "š” Go Back", callback_data="cbstart")
            ]]
        ))


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
