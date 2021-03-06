# (c) [Muhammed] @PR0FESS0R-99
# (s) @Mo_Tech_YT , @Mo_Tech_Group, @MT_Botz
# Copyright permission under MIT License
# All rights reserved by PR0FESS0R-99
# License -> https://github.com/PR0FESS0R-99/DonLee-Robot-V2/blob/Professor-99/LICENSE

import random
from pyrogram import filters, Client as DonLee_Robot_V2
from DonLee_Robot_V2.Config_Vars.Vars import Config
from DonLee_Robot_V2 import Text, Import, Database, LOGGER

db = Database()

@DonLee_Robot_V2.on_message(filters.command(["start", "alive"]) & filters.private)
async def start(bot: DonLee_Robot_V2, msg: Import.Msg):
    START_BUTTON = [[  
          Import.Button("β π π½π½ π¬πΎ π³π πΈπππ π’ππΊππ β", url=f"http://t.me/{Config.BOT_USERNAME}?startgroup=true")
          ],[
          Import.Button("β οΈ π§πΎππ", callback_data="help"),
          Import.Button("π π»πππ π€ ", callback_data="about")
          ]]
    if not await db.is_user_exist(msg.from_user.id):
        await db.add_user(msg.from_user.id)
    try:
        file_uid = msg.command[1]
    except IndexError:
        file_uid = False
             
    if file_uid:
        try:
            user = await bot.get_chat_member(Config.FORCE_CHANNEL, msg.chat.id)
            if user.status == "kicked out":
               await msg.reply_text("π π²ππππ π£ππ½πΎ, πΈππ πΊππΎ β οΈπ±οΈπ°οΈπ½οΈπ½οΈπ΄οΈπ³οΈβ οΈ")
               return
        except Import.User:
            userbot = await bot.get_me()
            await msg.reply_text(
                text=Config.FORCE_SUB_TEXT.format(msg.from_user.mention),
                reply_markup=Import.Markup([
                    [ Import.Button(text="π π©πππ", url=f"https://t.me/{Config.FORCE_CHANNEL}"),
                      Import.Button(text="π±πΎπΏππΎππ π", url=f"https://t.me/{Config.BOT_USERNAME}?start={file_uid}")]       
              ])
            )
            return

        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return

        if Config.CAPTION_BOLD_OR_MONO == "bold":
            caption = ("<b>" + file_name + "</b>")
        else:
            caption = ("<code>" + file_name + "</code>")
        try:
            await msg.reply_cached_media(
                file_id,
                quote=True,
                caption = f"""{caption}\n\n{Config.CUSTOM_CAPTION}""",
                parse_mode="html",
                reply_markup=db.Donlee_bt
            )

        except Exception as e:
            await msg.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    button = [[
     Import.Button('β Add Me To Your Groups β', url='http://t.me/donlee_robot?startgroup=true')
    ]]
    await msg.reply_photo(
    photo=random.choice(Config.PHOTO),
    caption=Text.START_TEXT.format(msg.from_user.mention, Config.DEV_ID),
    reply_markup=Import.Markup(START_BUTTON))


@DonLee_Robot_V2.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot: DonLee_Robot_V2, msg: Import.Msg):
        button = [[
          Import.Button("π ππππ₯ππππΎπ", callback_data="autofilter"),
          Import.Button("π¬πΊπππΊππ₯ππππΎπ", callback_data="filter"),
          Import.Button("π’ππππΎπΌπππππ", callback_data="connection")
          ],[
          Import.Button("π‘πΊπ", callback_data="ban"),
          Import.Button("π¬πππΎ", callback_data="mute"),
          Import.Button("π―ππππΎ", callback_data="purge")
          ],[
          Import.Button("π³πΎππΎπππΊπ―π", callback_data="telegraph"),
          Import.Button("π³π³π²", callback_data="tts"),
          Import.Button("π²πππΌππΎπ π¨π½", callback_data="sticker")
          ],[
          Import.Button("π’ππππππ", callback_data="country"),
          Import.Button("π¬πΎππΎ", callback_data="meme")
          ],[
          Import.Button("π’ππππ½", callback_data="covid"),
          Import.Button("π±πΎππππ", callback_data="report"),
          Import.Button("πΆπΎππΌπππΎ", callback_data="welcome")
          ],[
          Import.Button("π π§πππΎ", callback_data="home"),
          Import.Button("ππ²ππΊπππ", callback_data="status"),
          Import.Button("π π»ππππ€ ", callback_data="about")
          ]]
        await bot.send_photo(
            chat_id=msg.chat.id,
            photo=random.choice(Config.PHOTO),
            caption=Text.HELP_TEXT,
            reply_markup=Import.Markup(button),
            parse_mode="html", 
            reply_to_message_id=msg.message_id
        )



@DonLee_Robot_V2.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot: Keerthy bot, msg: Import.Msg):
        button = [[
          Import.Button("π¨βπ»Bot Owner contact", url='http://t.me/Keerthy_Owner_bot),
          Import.Button("π€", callback_data="source")
          ],[
          Import.Button("β οΈπ§πΎππ", callback_data="help"),
          Import.Button("π π§πππΎ", callback_data="home"),
          Import.Button("π’ππππΎποΈ", callback_data="close")
          ]]                     
        await bot.send_photo(
            chat_id=msg.chat.id,
            photo=random.choice(Config.PHOTO),
            caption=Text.ABOUT_TEXT.format(Config.BOT_USERNAME, Config.DEV_ID, Config.DEV_NAME, Config.BOT_USERNAME),
            reply_markup=Import.Markup(button),
            parse_mode="html", 
            reply_to_message_id=msg.message_id
        )


@DonLee_Robot_V2.on_message(filters.command(["sub", "subscribe"]) & filters.private, group=1)
async def sub(bot: Keerthy bot, msg: Import.Msg):
        button = [[     
          Import.Button("Movie file request bot", url="http://t.me/Keerthy_Owner_bot"),
          Import.Button("Movie Group 1π€", url="https://t.me/+CG7AQS6IfUNhYTNl")
          ],[
          Import.Button("π’π΄ππ½πΊππΎπ", url="https://t.me/+1qdEeHOTLdQ1M2Vl"),
          Import.Button("Movie Group 2π", url="https://t.me/+QNG5RF8mZK9mNjdl")
          ],[
          Import.Button("π€ Owner", url="http://t.me/Keerthy_Owner_bot"),
          Import.Button("π¨ππππΊπ", url="https://www.instagram.com/akshay_chand695")
          ],[
          Import.Button("π’ππππΎποΈ", callback_data="close")
          ]]                     
        await bot.send_photo(
            chat_id=msg.chat.id,
            photo=random.choice(Config.PHOTO),
            caption=Text.SUB_TEXT.format(Config.BOT_USERNAME, Config.DEV_ID, Config.DEV_NAME, Config.BOT_USERNAME),
            reply_markup=Import.Markup(button),
            parse_mode="html", 
            reply_to_message_id=msg.message_id
        )

@DonLee_Robot_V2.on_message(filters.private & filters.command("report"))
async def admin(bot, msg):
    button = [[  
       Import.Button("π’πππΌπ π§πΎππΎβ‘οΈ", url="t.me/Keerthy_Owner_bot")
       ]]
    await msg.reply_text(
        text="π’ππππΎπΌπ π‘πππππ π‘πΎππππ",
        reply_markup=Import.Markup(button)
    )
