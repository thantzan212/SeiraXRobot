import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SeiraRobot.events import register as MEMEK
from SeiraRobot import telethn as tbot

PHOTO = "https://telegra.ph/file/8c278d46b852306e18231.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  LUNA = "**Holla I'm Botညီလေး!** \n\n"
  LUNA += "💎 **I'm Working Properly** \n\n"
  LUNA += "💎 **My Master : [ဘူနံခန့်](https://t.me/olo_pl_ya_mal)** \n\n"
  LUNA += f"💎 **Telethon Version : {tlhver}** \n\n"
  LUNA += f"💎 **Pyrogram Version : {pyrover}** \n\n"
  LUNA += "**Thank for add my Botညီလေး 💜**"
  BUTTON = [[Button.url("Add Bot To Your Group", "https://t.me/n4nd4_hippy_bot?start=help"), Button.url("support", "https://t.me/+-Gsapl_ciLYwMGNl")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)

