import sys
import asyncio
import requests
import re
import string
from pyrogram.types import Message
from pyrogram import filters, Client
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from MatrixMusic import app

#استارت
@app.on_message(
    filters.command(["الاوامر"],""))
async def italy(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/a25271d31dd6e1bca849f.jpg",
        caption=f"""✅ **مرحبا بك عزيزي** {message.from_user.mention}
     
✅ **اليك قائمة اوامر سورس حـسـام ♬**
•𝅼▬▭࣪▬•| 𝑀𝐔𝑆𝐼𝐶 𝐻𝑂𝑆𝑆𝐴𝑀 |•▬▭࣪▬•
✅ **لـعـرض كـيـبـورد الأعــضــاء .**
»»»»»»  /hossam  ««««hossam«« .
•▬▭࣪▬•| 𝑀𝐔𝑆𝐼𝐶 𝐻𝑂𝑆𝑆𝐴𝑀 |•▬▭࣪▬•
**1 ← اوامـر الـمـجـمـوعـات .**
**2 ← اوامـر الـقـنـوات .**
**3 ← اوامـر الـبـوت .**
**4 ← مميزات السورس .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "◁ الـمـجـمـوعـات ▷", callback_data=f"italygro"),
                    InlineKeyboardButton(
                        "◁ الـقـنـوات ▷", callback_data=f"italycha"),
                ],[
                InlineKeyboardButton(
                        "◁ الـبـوت ▷", callback_data=f"italybot"),
                ],[
                InlineKeyboardButton(
                        "◁ السورس ▷", callback_data=f"italysou"),
                ],[
                    InlineKeyboardButton(
                        "𝑀𝐔𝑆𝐼𝐶 𝐻𝑂𝑆𝑆𝐴𝑀", callback_data=f"italydev"),
                ],[
                    InlineKeyboardButton(
                        "اغــلاق ♬", callback_data=f"close"),
               ],
            ]
        ),
    )
#كول باك اوامر المجموعه
@app.on_callback_query(filters.regex("italygro"))
async def italy(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ **اليك قائمة اوامر المجموعات ♬**
•▬▭࣪▬•| 𝑀𝐔𝑆𝐼𝐶 𝐻𝑂𝑆𝑆𝐴𝑀 |•▬▭࣪▬•
**- لتشغيل اغنيه اكتب : تشغيل او شغل .**
**- لتشغيل فيديو اكتب : فيديو .**
**- لأنهاء الاغنيه اكتب : ايقاف او انهاء .**
**- لتخطي الاغنيه اكتب : تخطي .**
**-اذا حدث خطأ او اعادة التشغيل اكتب :** /restart .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "◁ الـقـنـوات ▷", callback_data=f"italycha"),
                    InlineKeyboardButton(
                        "◁ الـبـوت ▷", callback_data=f"italybot"),
                ],[
                InlineKeyboardButton(
                        "◁ السورس ▷", callback_data=f"italysou"),
                ],[
                    InlineKeyboardButton(
                        "𝑀𝐔𝑆𝐼𝐶 𝐻𝑂𝑆𝑆𝐴𝑀", callback_data=f"italydev"),
                ],[
                    InlineKeyboardButton(
                        "اغــلاق ♬", callback_data=f"close"),
               ],
            ]
        ),
    )
#كول باك اوامر القناه
@app.on_callback_query(filters.regex("italycha"))
async def italy(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ **اليك قائمة اوامر الـقـنـوات ♬**
•▬▭࣪▬•| 𝑀𝐔𝑆𝐼𝐶 𝐻𝑂𝑆𝑆𝐴𝑀 |•▬▭࣪▬•
**- لتشغيل اغنيه اكتب : تشغيل او شغل .**
**- لتشغيل فيديو اكتب : فيديو .**
**- لأنهاء الاغنيه اكتب : ايقاف او انهاء .**
**- لتخطي الاغنيه اكتب : تخطي .**
**-اذا حدث خطأ او اعادة التشغيل اكتب :** /restart .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "◁ الـمـجـمـوعـات ▷", callback_data=f"italygro"),
                    InlineKeyboardButton(
                        "◁ الـبـوت ▷", callback_data=f"italybot"),
                ],[
                InlineKeyboardButton(
                        "◁ السورس ▷", callback_data=f"italysou"),
                ],[
                    InlineKeyboardButton(
                        "𝑀𝐔𝑆𝐼𝐶 𝐻𝑂𝑆𝑆𝐴𝑀", callback_data=f"italydev"),
                ],[
                    InlineKeyboardButton(
                        "اغــلاق ♬", callback_data=f"close"),
               ],
            ]
        ),
    )
#كول باك اوامر البوت
@app.on_callback_query(filters.regex("italybot"))
async def italy(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ **اليك قائمة اوامر الـبـوت ♬**
•▬▭࣪▬•| 𝑀𝐔𝑆𝐼𝐶 𝐻𝑂𝑆𝑆𝐴𝑀 |•▬▭࣪▬•
**- لعمل اذاعه في البوت قم برد علي الاذاعه واكتب : اذاعه .**
 **- لعرض احصائيات البوت اكتب : الاحصائيات .**
**- لعرض سرعه البوت اكتب : بينج .**
**- للتحكم في لغه البوت اكتب : اللغه .**
**- للتحكم في وضع التشغيل اكتب : الاعدادات .**
**- اوامر الحظر والرفع في كيبورد المطور .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "◁ الـمـجـمـوعـات ▷", callback_data=f"italygro"),
                    InlineKeyboardButton(
                        "◁ الـقـنـوات ▷", callback_data=f"italycha"),
                ],[
                InlineKeyboardButton(
                        "◁ السورس ▷", callback_data=f"italysou"),
                ],[
                    InlineKeyboardButton(
                        "𝑀𝐔𝑆𝐼𝐶 𝐻𝑂𝑆𝑆𝐴𝑀", callback_data=f"italydev"),
                ],[
                    InlineKeyboardButton(
                        "اغــلاق ♬", callback_data=f"close"),
               ],
            ]
        ),
    )
#كول باك اوامر مميزات السورس
@app.on_callback_query(filters.regex("italysou"))
async def italy(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ **اليك قائمة اوامر سورس حـسـام ♬**
   المس الامر لنسخ والاستخدام
•▬▭࣪▬•| 𝑀𝐔𝑆𝐼𝐶 𝐻𝑂𝑆𝑆𝐴𝑀 |•▬▭࣪▬•
**- لعرض كليشه السورس اكتب :** `سورس` .
**- لعرض مين في الكول اليك الامر  :** `مين في الكول` .
**- لزخرفه عربي او انجلش اكتب  :** `فه واسم الزخرفه مثال زخرفه hossam .` .
**- لعرض بوت الحذف اكتب   :** `بوت حذف` .
**- لعمل كت او تويت اليك الامر  :** `كت او تويت` .
**- لعرض مطور البوت اكتب :** `المطور` .
**- لعرض اسم البوت اكتب :** `بوت` .
**- لعرض الايدي الخاص بك في الجروب او البرايفت اكتب :** `ا` او `ايدي` .
**- لصناعة رابط تليجراف ارسل الصوره برد عليه :** `تليجراف` .
**- لعرض لينك الجروب ارسل :** `لينك` او `رابط` .
**- لطباعة صوره علي التريمنال ارسل الرساله انجليزي برد عليه :** `طباعه` .
**- لترجمة نص مثال :** /tr ar hossam
**- لتحويل ملصق الي صورة قم برد علي الملصق :** `pict` .
**- لتحويل الصوره الي ملصق قم برد علي الملصق :** `stik` .
**- لعرض كود الملصق قم برد علي الملصق :** `code` .
**- لعرض اسمك اكتب :** `اسمي` .
**- لمعرفة معلومات شخص قم برد عليه :** `كشف` .
**- لعمل تاك للاعضاء استخدم امر :** `تاك` .
**- لايقاف تاك للاعضاء استخدم امر :** `/cancel` .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "◁ الـمـجـمـوعـات ▷", callback_data=f"italygro"),
                    InlineKeyboardButton(
                        "◁ الـقـنـوات ▷", callback_data=f"italycha"),
                ],[
                InlineKeyboardButton(
                        "◁ الـبـوت ▷", callback_data=f"italybot"),
                ],[
                    InlineKeyboardButton(
                        "𝑀𝐔𝑆𝐼𝐶 𝐻𝑂𝑆𝑆𝐴𝑀", callback_data=f"italydev"),
                ],[
                    InlineKeyboardButton(
                        "اغــلاق ♬", callback_data=f"close"),
               ],
            ]
        ),
    )
#كول باك المطورين
@app.on_callback_query(filters.regex("italydev"))
async def ayamr(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""[ٓ♡ | 𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑺𝑶𝑼𝑹𝑪𝑬 𝐻𝑂𝑆𝑆𝐴𝑀  .](https://t.me/UU_GR)\n\n[♡ | 𝐻𝑂𝑆𝑆𝐴𝑀  𝑻𝑯𝑬 𝑩𝑬𝑺𝑻 𝑺𝑶𝑼𝑹𝑪𝑬 𝑶𝑵 𝑻𝑬𝑳𝑬 .](https://t.me/UU_GR)\n\n[♡ | 𝑭𝑶𝑳𝑳𝑶𝑾 𝑻𝑯𝑬 𝑩𝑼𝑻𝑻𝑶𝑵𝑺 𝑩𝑬𝑳𝑶𝑾 .](https://t.me/UU_GR)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝑯𝑶𝑺𝑺𝑨𝑴 𝑨𝑳 𝑯𝑶𝑳𝑨𝑵𝑫𝒀 ✶ ✶🇳🇱", url=f"https://t.me/H_OS_S_AM"), 
                ],[               
                    InlineKeyboardButton(
                        "اغــلاق ♬", callback_data=f"close"),
               ],
            ]
        ),
    )
