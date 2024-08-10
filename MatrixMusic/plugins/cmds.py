import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from MatrixMusic import app
from config import OWNER_ID, LOGGER_ID


@app.on_message(command(["الاوامر"]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    await message.reply_photo(
        photo=f"https://telegra.ph/file/a25271d31dd6e1bca849f.jpg",
        caption=f"""<b>↯︙مرحباً بك عزيزي</b>\n<b>↯︙استخدم الازرار بالاسفل\n» ل تصفح اوامر الميوزك</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ اوامر التشغيل ›", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "‹ اوامر القناة ›", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "‹ اوامر الادمن ›", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "‹ اوامر المطور ›", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(name, url=f"https://t.me/{usrnam}"),
                ],[
                    InlineKeyboardButton(
                        "𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑶𝑺𝑺𝑨𝑴", url="https://t.me/UU_GR"),
                   ],
            ]
        ),
    )     
         

@app.on_callback_query(filters.regex("zzzdv"))
async def mpdtsf(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""<b>↯︙مرحباً بك عزيزي المطور </b>\n\n<b>↯︙استخدم الازرار بالاسفل\n↯︙ل تصفح اوامر الميوزك</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ التحديث ›", callback_data="zzzup"),
                ],[
                    InlineKeyboardButton(
                        "‹ الرفع ›", callback_data="zzzsu"),
                    InlineKeyboardButton(
                        "‹ الحظر ›", callback_data="zzzbn"),
                ],[
                    InlineKeyboardButton(
                        "‹ اشعارات & المساعد ›", callback_data="zzzas"),
                ],[
                    InlineKeyboardButton(
                        "‹ رجوع ›", callback_data="zzzback"),
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("zzzll"))
async def zzzll(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯︙<b>قائمة اوامر التشغيل :</b>
– – – – – – – – – – – – – – – – – –
تشغيل + (اسم الاغنية / رابط الاغنية)
<b>- ل تشغيل اغنية في المكالمة الصوتية</b>
– – – – – – – – – – – – – – – – – –
فيديو + (اسم المقطع / رابط المقطع)
<b>- ل تشغيل فيديو في المكالمة المرئية</b>
– – – – – – – – – – – – – – – – – –
بحث + الاسم
<b>- ل تحميل الاغاني والمقاطع الصوتيه من اليوتيوب</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzad"))
async def zzzad(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯︙<b>قائمة اوامر الادمن :</b>
– – – – – – – – – – – – – – – – – –
الاعدادات
<b>- ل عرض إعدادات اوضاع التشغيل</b>
– – – – – – – – – – – – – – – – – –
ايقاف / انهاء / اسكت
<b>- ل إيقاف تشغيل الموسيقى في المكالمة</b>
– – – – – – – – – – – – – – – – – –
وقف / توقف
<b>- ل إيقاف تشغيل الموسيقى في المكالمة مؤقتاً</b>
– – – – – – – – – – – – – – – – – –
كمل / كملي
<b>- ل إستئناف تشغيل الموسيقى في المكالمة</b>
– – – – – – – – – – – – – – – – – –
تخطي
<b>- ل تخطي الاغنية وتشغيل الاغنية التاليه</b>
– – – – – – – – – – – – – – – – – –
الاغاني
<b>- ل معرفة الاغاني الموجودة في قائمة الانتظار</b>
– – – – – – – – – – – – – – – – – –
بنج
<b>- ل عرض سرعة تشغيل البوت</b>
– – – – – – – – – – – – – – – – – –
رفع ادمن/تنزيل ادمن
<b>- ل رفع/تنزيل ادمن في البوت</b>
– – – – – – – – – – – – – – – – – –
الادمنيه
<b>- ل عرض قائمة ادمنية البوت</b>
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzch"))
async def zzzch(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯︙<b>قائمة اوامر التشغيل في القناة :</b>
– – – – – – – – – – – – – – – – – –
<b>- ارفع البوت إشراف في القناة و شغل مباشر</b>
<b>- ارسل (/channelplay او ربط) + يوزر القناة ل الربط</b>
<b>- ثم استخدم الاوامر بالاسفل ل التشغيل</b>
– – – – – – – – – – – – – – – – – –
تشغيل + اسم الاغنية
<b>- ل تشغيل اغنية في المكالمة الصوتية</b>
– – – – – – – – – – – – – – – – – –
فيديو + اسم المقطع
<b>- ل تشغيل فيديو في المكالمة المرئية</b>
– – – – – – – – – – – – – – – – – –
ايقاف / انهاء / اسكت
<b>- ل إيقاف تشغيل الموسيقى في المكالمة</b>
– – – – – – – – – – – – – – – – – –
وقف / توقف
<b>- ل إيقاف تشغيل الموسيقى في المكالمة مؤقتاً</b>
– – – – – – – – – – – – – – – – – –
كمل / استئناف
<b>- ل إستئناف تشغيل الموسيقى في المكالمة</b>
– – – – – – – – – – – – – – – – – –
تخطي
<b>- ل تخطي الاغنية وتشغيل الاغنية التاليه</b>
– – – – – – – – – – – – – – – – – –
/seek + عدد الثواني
<b>- ل تقديم الاغنيه ل الامام</b>
/seekback + عدد الثواني
<b>- ل إرجاع الاغنيه ل الخلف</b>
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzup"))
async def zzzup(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯︙<b>قائمة اوامر المطور :</b>
– – – – – – – – – – – – – – – – – –
<b>- قائمة اوامر التحديثات :</b>
– – – – – – – – – – – – – – – – – –
السجلات
<b>- لـ جلب سجلات البوت</b>
– – – – – – – – – – – – – – – – – –
تحديث
<b>- لـ تحديث البوت</b>
– – – – – – – – – – – – – – – – – –
اعاده تشغيل
<b>- لـ اعادة تشغيل البوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzsu"))
async def zzzsu(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯︙<b>قائمة اوامر المطور :</b>
– – – – – – – – – – – – – – – – – –
<b>- قائمة اوامر الرفع :</b>
– – – – – – – – – – – – – – – – – –
رفع مطور/تنزيل مطور
<b>- ل رفع/تنزيل شخص مطور في ميوزك البوت</b>
– – – – – – – – – – – – – – – – – –
المطورين
<b>- ل عرض قائمة مطورين البوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzbn"))
async def zzzbn(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯︙<b>قائمة اوامر المطور :</b>
– – – – – – – – – – – – – – – – – –
<b>- قائمة اوامر الحظر :</b>
– – – – – – – – – – – – – – – – – –
بلوك/الغاء بلوك/المبلكين
<b>- ل حظر/الغاء حظر شخص من استخدام ميوزك البوت</b>
– – – – – – – – – – – – – – – – – –
احظره عام/الغاء حظره عام
<b>- ل حظر/الغاء حظر شخص من استخدام ميوزك البوت عام</b>
– – – – – – – – – – – – – – – – – –
المحظورين عام
<b>- ل جلب قائمة المحظورين عام في البوت</b>
– – – – – – – – – – – – – – – – – –
حظر مجموعة/سماح
<b>- ل حظر/الغاء حظر مجموعة من استخدام ميوزك البوت</b>
– – – – – – – – – – – – – – – – – –
المجموعات المحظورة
<b>- ل جلب قائمة بالمجموعات المحظورة من استخدام البوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )


@app.on_callback_query(filters.regex("zzzas"))
async def zzzas(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯︙<b>قائمة اوامر المطور :</b>
– – – – – – – – – – – – – – – – – –
<b>↯︙قائمة اوامر المساعد :</b>
– – – – – – – – – – – – – – – – – –
السجل ⦗ تفعيل / تعطيل ⦘
<b>- ل تفعيل/تعطيل اشعارات مجموعة سجل البوت</b>
– – – – – – – – – – – – – – – – – –
⦗ المغادره التلقائيه ⦗ تفعيل / تعطيل
<b>- ل تفعيل/تعطيل المغادره التلقائيه ل الحساب المساعد من المجموعات عند عدم استخدام الميوزك</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "‹ رجوع ›", callback_data="zzzdv"),
               ],
          ]
        ),
   )
