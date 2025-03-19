from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PrinceMusic import app
from config import BOT_USERNAME
from PrinceMusic.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**⌾ ᴡᴇʟᴄᴏᴍᴇ ғᴏʀ ᴘʀɪɴᴄᴇ ʀᴇᴘᴏs ⌾
 
● ɪғ ʏᴏᴜ ᴡᴀɴᴛ ˹ ᴘʀɪɴᴄᴇ ꭙ ᴍᴜsɪᴄ ♡゙゙

● ʙᴏᴛ ʀᴇᴘᴏ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ● **
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✙ ᴀᴅᴅ ᴍᴇ ✙", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ʜᴇʟᴘ •", url="https://t.me/ll_SMARTY_PRINCE_ll"),
          InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="https://t.me/ll_SMARTY_PRINCE_ll"),
          ],
               [
                InlineKeyboardButton("• ɴᴇᴛᴡᴏʀᴋ •", url=f"https://t.me/l_ABOUT_PRINCE_l"),
],
[
InlineKeyboardButton("• ʀᴇᴘᴏ •", url=f"https://github.com/RishuBot/RishuManagement"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://envs.sh/oK4.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
