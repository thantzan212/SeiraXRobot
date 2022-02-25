import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SeiraRobot.events import register as MEMEK
from SeiraRobot import telethn as tbot

PHOTO = "https://telegra.ph/file/8c278d46b852306e18231.jpg"

@MEMEK(pattern=("/mdown"))
async def awake(event):
  tai = event.sender.first_name
  LUNA = "** ──「 Perintah Dasar 」── ** \n\n"
  LUNA += "• /play **(nama lagu / balas ke audio) — play musik via YouTube** \n"
  LUNA += "• /vplay ** (nama lagu / balas ke audio) – play video stream via YouTube** \n"
  LUNA += "• /playlist - **Untuk memutar playlist Anda atau playlist group anda** \n"
  LUNA += "• /song - ** (nama lagu) mendownload lagu via YouTube** \n\n"
  LUNA += "** ──「 Admin CMD 」── ** \n\n"
  LUNA += "• /music on|off - **mengaktifkan atau menonaktifkan music player di grup anda** \n"
  LUNA += "• /pause atau /vpause - **Untuk pause musik/video yang sedang di putar** \n"
  LUNA += "• /resume atau /vresume - **Untuk melanjutkan musik/video yang sedang ter pause** \n"
  LUNA += "• /skip - **Untuk melewati lagu berikutnya** \n"
  LUNA += "• /end - **Untuk memberhentikan pemutaran musik** \n"
  LUNA += "• /vstop - **Untuk memberhentikan video stream yang sedang diputar** \n"
  LUNA += "• /reload - **Untuk memperbarui admin list** \n"

  BUTTON = [[Button.url("☎️ Support", "https://t.me/beginmer_2015"), Button.url("📡 Updates", "https://t.me/beginner_2015")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)
