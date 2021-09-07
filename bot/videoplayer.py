import os
import re
import pafy
import time
import asyncio
import ffmpeg
from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import GroupCallFactory
from youtube_dl import YoutubeDL
from pytube import YouTube
from youtube_search import YoutubeSearch

from config import API_ID, API_HASH, SESSION_NAME, BOT_USERNAME
from helpers.decorators import authorized_users_only
from helpers.filters import command


def video_link_getter(url: str):
    yt = YouTube(url)
    x = yt.streams.filter(file_extension="mp4", res="720p")[0].download("downloads")
    return x

ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True,
}
ydl = YoutubeDL(ydl_opts)

STREAM = {8}
VIDEO_CALL = {}

app = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
)
group_call_factory = GroupCallFactory(app, GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM)


@Client.on_message(command(["vstream", f"vstream@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def startvideo(client, m: Message):
    replied = m.reply_to_message
    if not replied:
        if len(m.command) < 2:
            await m.reply("💡 Reply to video or provide youtube video url to start video streaming")
        else:
            video = " ".join(m.command[1:])
            youtube_regex = (
                r'(https?://)?(www\.)?'
                '(youtube|youtu|youtube-nocookie)\.(com|be)/'
                '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
            youtube_regex_match = re.match(youtube_regex, video)
            if youtube_regex_match:
                try:
                    x = video_link_getter(video)
                except Exception as e:
                    await m.reply(f"🚫 **Error** - `{e}`")
                    return
                msg = await m.reply("🔁 **Starting video streaming...**")
                chat_id = m.chat.id
                await asyncio.sleep(1)
                try:
                    group_call = group_call_factory.get_group_call()
                    await group_call.join(chat_id)
                    await group_call.start_video(x, repeat=False)
                    VIDEO_CALL[chat_id] = group_call
                    await msg.edit((f"💡 **Started [video streaming]({x}) !\n\n» Join to video chat on the top to watch streaming."), disable_web_page_preview=True)
                except Exception as e:
                    await msg.edit(f"🚫 **Error** - `{e}`")
            	
    elif replied.video or replied.document:
        msg = await m.reply("📥 Downloading video...")
        video = await client.download_media(m.reply_to_message)
        chat_id = m.chat.id
        await asyncio.sleep(2)
        try:
            group_call = group_call_factory.get_group_call()
            await group_call.join(chat_id)
            await group_call.start_video(video, repeat=False)
            VIDEO_CALL[chat_id] = group_call
            await msg.edit("💡 **Video streaming started!**\n\n» **Join to video chat to watch the video.**")
        except Exception as e:
            await msg.edit(f"**🚫 Error** - `{e}`")
    else:
        await m.reply("💭 Please reply to video or video file to stream")


@Client.on_message(command(["vstop", f"vstop@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def stopvideo(client, m: Message):
    chat_id = m.chat.id
    try:
        await VIDEO_CALL[chat_id].stop()
        await m.reply("✅ **Streaming has ended successfully !**")
    except Exception as e:
        await m.reply(f"🚫 **Error** - `{e}`")
