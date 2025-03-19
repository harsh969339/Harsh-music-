from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PrinceMusic import app
from config import BOT_USERNAME
from PrinceMusic.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬─────────────────⦿
│├─────────────────╮
│├ ᴛɢ ɴᴀᴍᴇ - ᴘʀɪɴᴄᴇ sᴀɴᴀᴛᴀɴɪ
│├ ʀᴇᴀʟ ɴᴀᴍᴇ - ᴘʀɪɴᴄᴇ ʀᴀᴊᴘᴜᴛ
│├─────────────────╯
├┼─────────────────⦿
├┤~ @RishuNetwork
├┤~ @Ur_rishu_143
├┤~ @Vip_robotz
├┼─────────────────⦿
│├─────────────────╮
│├OWNER│ @ll_SMARTY_PRINCE_ll
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("Ｒ I Տ ᕼ ᑌ ", url=f"https://t.me/ll_SMARTY_PRINCE_ll")
        ],
        [
          InlineKeyboardButton("ＨＥＬＰ", url="https://t.me/ll_SMARTY_PRINCE_ll"),
          InlineKeyboardButton("ＲＥＰＯ", url="https://github.com/RishuBot/RishuManagement"),
          ],
               [
                InlineKeyboardButton(" ＮＥＴＷＯＲＫ", url=f"https://t.me/l_ABOUT_PRINCE_l"),
],
[
InlineKeyboardButton("ＯＦＦＩＣＩＡＬ ＢＯＴ", url=f"https://t.me/vip_music_vc_bot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://envs.sh/oKU.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
