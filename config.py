import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "27026389")
    API_HASH  = os.environ.get("API_HASH", "158b014213c39d3b342a8792e495a5dc")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6402185585:AAEipQ2sRiehtofziBiJzbYc2PgQ67fw858") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","Cluster0")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://Hunterbots:Hunterbots@cluster0.il15reh.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/804eb7fffdb95208a7123.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1601545124').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "fsremote") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001843978274))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """<b>HI {} 👋,
      𝐒𝐨𝐲 𝐑𝐞𝐧𝐚𝐦𝐞 𝐅𝐢𝐥𝐞𝐬 𝐁𝐨𝐭
𝐏𝐮𝐞𝐝𝐨 𝐜𝐚𝐦𝐛𝐢𝐚𝐫 𝐞𝐥 𝐧𝐨𝐦𝐛𝐫𝐞 𝐲 𝐦𝐢𝐧𝐢𝐚𝐭𝐮𝐫𝐚 𝐝𝐞 𝐬𝐮 𝐚𝐫𝐜𝐡𝐢𝐯𝐨 𝐝𝐞 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦.
𝐓𝐚𝐦𝐛𝐢é𝐧 𝐩𝐮𝐞𝐝𝐞 𝐜𝐨𝐧𝐯𝐞𝐫𝐭𝐢𝐫 𝐮𝐧 𝐯í𝐝𝐞𝐨 𝐚 𝐚𝐫𝐜𝐡𝐢𝐯𝐨 𝐲 𝐚𝐫𝐜𝐡𝐢𝐯𝐨 𝐚 𝐯í𝐝𝐞𝐨.
𝐄𝐥 𝐁𝐨𝐭 𝐭𝐚𝐦𝐛𝐢é𝐧 𝐚𝐝𝐦𝐢𝐭𝐞 𝐬𝐮𝐛𝐭í𝐭𝐮𝐥𝐨𝐬 𝐩𝐞𝐫𝐬𝐨𝐧𝐚𝐥𝐢𝐳𝐚𝐝𝐨𝐬 𝐲 𝐦𝐢𝐧𝐢𝐚𝐭𝐮𝐫𝐚𝐬 𝐩𝐞𝐫𝐬𝐨𝐧𝐚𝐥𝐢𝐳𝐚𝐝𝐚𝐬. 
>> 𝐂𝐫𝐞𝐚𝐝𝐨 𝐩𝐨𝐫 @𝐟𝐞𝐟𝐭𝟎𝟓 <<⚡💙</b>"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 My Name : {}
├🖥️ Desarrollador : <a href=https://t.me/fsremote>Network</a> 
├👨‍💻 Programador: <a href=@feft05>FɛʄȶϟHUNTER</a>
├📕 Library : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
├✏️ Lenguaje: <a href=https://www.python.org>Pyᴛʜᴏɴ 3</a>
├💾 DB: <a href=https://cloud.mongodb.com>Mongo DB</a>
├📊 Build Version: <a href=https://github.com/> V3.0.0</a></b>     
╰───────────────⍟ """

    HELP_TXT = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ</u></b>
  
<b>•></b> /start Tʜᴇ Bᴏᴛ Aɴᴅ Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ.
📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>
<b>•></b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
Exᴀᴍᴩʟᴇ:- /set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}
✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>•></b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nɴᴀᴍᴇ \nAɴᴅ Aᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].           
ℹ️ 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/feft05>𝑺𝑼𝑷𝑷𝑶𝑹𝑻</a>
"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""
