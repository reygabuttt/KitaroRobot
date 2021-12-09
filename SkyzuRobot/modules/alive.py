import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SkyzuRobot.events import register
from SkyzuRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/68592ad5407730bd6d610.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hey [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Kitaro Robot.** \n\n"
  TEXT += "🔰 **I'm Working Now** \n\n"
  TEXT += f"🔰 **My Master : [Kitaro](https://t.me/Kitarohey)** \n\n"
  TEXT += f"🔰 **Library Version :** `{telever}` \n\n"
  TEXT += f"🔰 **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"🔰 **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here 🙏**"
  BUTTON = [[Button.url("SUPPORT GROUP", "https://t.me/rumahkitaro"), Button.url("CHANNEL​", "https://t.me/hariannsayaa")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
