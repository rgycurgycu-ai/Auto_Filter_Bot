import re
import os
from os import environ, getenv
from Script import script

# Utility functions
id_pattern = re.compile(r'^-?\d+$')  # corrected regex to match negative ids too

def is_enabled(value, default):
    if str(value).lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif str(value).lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# ============================
# Bot Information Configuration
# ============================
SESSION = environ.get('SESSION', 'dreamxbotz_search')   # Session name for the bot
API_ID = int(environ.get("API_ID", 21643763))           # Make sure env variable is numbers only
API_HASH = environ.get('API_HASH', '9ab0b0e819951db76417c7e4962ccdf5')  
BOT_TOKEN = environ.get('BOT_TOKEN', "7262086950:AAEosy2Wjdgp-r1gnuCq8rIWu_-VmwCfobE")

# ============================
# Bot Settings
# ============================
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled(environ.get('USE_CAPTION_FILTER', True), True)
INDEX_CAPTION = is_enabled(environ.get('SAVE_CAPTION', True), True)

PICS = environ.get('PICS', 'https://envs.sh/4Y1.jpg').split()
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/e20b5fdaf217252964202.jpg")
MELCOW_PHOTO = environ.get("MELCOW_PHOTO", "https://graph.org/file/56b5deb73f3b132e2bb73.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/13702ae26fb05df52667c.jpg")

# ============================
# Admins & Channels
# ============================
ADMINS = [int(admin) if id_pattern.match(admin) else admin for admin in environ.get('ADMINS', '5095951697').split()]
CHANNELS = [int(ch) if id_pattern.match(ch) else ch for ch in environ.get('CHANNELS', '-1001448525970').split()]

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1003103968429'))
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1003103968429'))
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-1003103968429'))
DELETE_CHANNELS = [int(dch) if id_pattern.match(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-100').split()]
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-100')
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002767321414')

# FORCE_SUB
auth_req_channels = environ.get("AUTH_REQ_CHANNELS", "-1002767321414")
auth_channels     = environ.get("AUTH_CHANNELS", "-1002711680347")

# ============================
# MongoDB
# ============================
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Rahul:Rahulalppatta@cluster0.vswch4c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'dreamcinezone_files')
MULTIPLE_DB = is_enabled(environ.get('MULTIPLE_DB', False), False)
DATABASE_URI2 = environ.get('DATABASE_URI2', "")

# ============================
# TMDB & Movie Settings
# ============================
TMDB_API_KEY = environ.get('TMDB_API_KEY', '')
TMDB_POSTER = is_enabled(environ.get('TMDB_POSTER', False), False)
LANDSCAPE_POSTER = is_enabled(environ.get('LANDSCAPE_POSTER', True), True)

# ============================
# Channels & Force Sub Lists
# ============================
AUTH_REQ_CHANNELS = [int(ch) for ch in auth_req_channels.split() if ch and id_pattern.match(ch)]
AUTH_CHANNELS = [int(ch) for ch in auth_channels.split() if ch and id_pattern.match(ch)]
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.match(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.match(support_chat_id) else None

# ============================
# Misc
# ============================
ULTRA_FAST_MODE = is_enabled(environ.get('ULTRA_FAST_MODE', False), True)
PORT = int(environ.get("PORT", "8080"))
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")

# ============================
# Reactions & Commands
# ============================
REACTIONS = ["🤝","😇","🤗","😍","👍","🎅","😐","🥰","🤩","😱","🤣","😘","👏","😛","😈","🎉","⚡️","🫡","🤓","😎","🏆","🔥","🤭","🌚","🆒","👻","😁"]
Bot_cmds = {
    "start": "Sᴛᴀʀᴛ Mᴇ Bᴀʙʏ",
    "stats": "Gᴇᴛ Bᴏᴛ Sᴛᴀᴛs",
    "alive": " Cʜᴇᴄᴋ Bᴏᴛ Aʟɪᴠᴇ ᴏʀ Nᴏᴛ "
}

