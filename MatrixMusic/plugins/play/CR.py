import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from MatrixMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","السورس"])
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/a25271d31dd6e1bca849f.jpg",
        caption=f"""W𝐞𝐥𝐨𝐦𝐞 𝐭𝐨 𝐬𝐨𝐮𝐫𝐜𝐞 𝐡𝐨𝐬𝐬𝐚𝐦 𝐦𝐮𝐬𝐢𝐜""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "G𝑟𝑜𝑢𝑝", url=f"https://t.me/A_X_l_X"), 
                 InlineKeyboardButton(
                   "𝑺𝑶𝑼𝑹𝑪𝑬 ",       url=f"https://t.me/UU_GR"), 
                 
             ],[ 
            InlineKeyboardButton(
                        "𓏺 𝐇𝐎𝐒𝐒𝐀𝐌 𝐇𝐎𝐋𝐍𝐃𝐀 ✶ ✶🇳🇱", url=f"https://t.me/H_OS_S_AM"), 
                   
             ],[ 
                  InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك⚡",
                url=f"https://t.me/{app.username}?startgroup=true"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["المطور حسام"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("H_OS_S_AM")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"معلومات مطور السورس\n\n‍ ¦dev :{name}\n\n ¦user :@{usr.username}\n\n ¦id :`{usr.id}`\n\n ¦bio :{usr.bio}\n\n𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑶𝑺𝑺𝑨𝑴", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["الهولندي" , "حسام","مبرمج السورس"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("H_OS_S_AM")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"معلومات مطور السورس.\n\n¦dev :{name}\n\n ¦user :@{usr.username}\n\n ¦id :`{usr.id}`\n\n ¦boi :{usr.bio}\n\n𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑶𝑺𝑺𝑨𝑴", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )



@app.on_message(
    command(["مطور السورس" , "هيثوم","هيثم"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat(".")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"معلومات مبرمج السورس.\n\n¦dev :{name}\n\n ¦user :@{usr.username}\n\n ¦id :`{usr.id}`\n\n ¦bio :{usr.bio}\n\n𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑶𝑺𝑺𝑨𝑴", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )



