# Infinity Bots

from pyrogram import Client, filters

@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
  await message.reply("Hey there, I'm πͺπ¨π·π»π°πΆπ΅ π¬π«π°π»πΆπΉ π©πΆπ».\nI can add a caption for every document file sent to a channel. \n\nPowered by => https://t.me/epusthakalaya_bots \n\n**@EPUSTHAKALAYABOTz**")
