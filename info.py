import re
import os
from os import environ

# ============================
# Utility Functions
# ============================

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default=False):
    """Return True/False for environment values like yes/true/1"""
    if str(value).lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif str(value).lower() in ["false", "no", "0", "disable", "n"]:
        return False
    return default


# ============================
# Basic Bot Info
# ============================

SESSION = environ.get("SESSION", "mybot_session")
API_ID = int(environ.get("API_ID", "21643763"))        # From my.telegram.org
API_HASH = environ.get("API_HASH", "9ab0b0e819951db76417c7e4962ccdf5") # From my.telegram.org
BOT_TOKEN = environ.get("BOT_TOKEN", "7262086950:AAEGJsxnD9UeKwLUnkTueikhVofTwuyho6w")  # From @BotFather


# ============================
# Admins & Channels
# ============================

ADMINS = [int(x) for x in environ.get("ADMINS", "5095951697").split()]
CHANNELS = [int(x) for x in environ.get("CHANNELS", "-1003186766542").split()]
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003142539096"))


# ============================
# Database Config
# ============================

DATABASE_URI = environ.get("mongodb+srv://Rahul:Rahulalppatta@cluster0.vswch4c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "mongodb+srv://...")
DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
COLLECTION_NAME = environ.get("COLLECTION_NAME", "bot_files")


# ============================
# Bot Settings
# ============================

CACHE_TIME = int(environ.get("CACHE_TIME", 600))
USE_CAPTION_FILTER = is_enabled(environ.get("USE_CAPTION_FILTER", "True"))
AUTO_DELETE = is_enabled(environ.get("AUTO_DELETE", "True"))
PROTECT_CONTENT = is_enabled(environ.get("PROTECT_CONTENT", "False"))
SPELL_CHECK = is_enabled(environ.get("SPELL_CHECK", "True"))

# Images
PICS = environ.get("PICS", "https://graph.org/file/sample.jpg").split()
LOGO_IMG = environ.get("LOGO_IMG", "https://graph.org/file/logo.jpg")

# ============================
# Premium / Payment Config
# ============================

QR_CODE = environ.get("QR_CODE", "https://graph.org/file/payment_qr.jpg")
OWNER_UPI_ID = environ.get("OWNER_UPI_ID", "not_available")

PREMIUM_PLANS = {
    10: "7days",
    20: "15days",
    50: "1month"
}


# ============================
# TMDB / IMDB Config
# ============================

IMDB = is_enabled(environ.get("IMDB", "True"))
TMDB_API_KEY = environ.get("TMDB_API_KEY", "your_tmdb_key")
LONG_DESCRIPTION = is_enabled(environ.get("LONG_DESCRIPTION", "False"))


# ============================
# Miscellaneous
# ============================

OWNER_ID = int(environ.get("OWNER_ID", "123456789"))
SUPPORT_GROUP = environ.get("SUPPORT_GROUP", "https://t.me/YourGroup")
UPDATE_CHANNEL = environ.get("UPDATE_CHANNEL", "https://t.me/YourChannel")
DELETE_TIME = int(environ.get("DELETE_TIME", 300))
CUSTOM_CAPTION = environ.get("CUSTOM_CAPTION", "Uploaded by MyBot")

REACTIONS = ["🔥", "😍", "😎", "😁", "⚡️", "🎉", "👏"]

# ============================
# Log Summary
# ============================

LOG_STR = f"""
✅ CONFIGURATION SUMMARY ✅

BOT SESSION: {SESSION}
ADMINS: {ADMINS}
CHANNELS: {CHANNELS}
LOG CHANNEL: {LOG_CHANNEL}
DATABASE: {DATABASE_NAME}
CACHE TIME: {CACHE_TIME}s
USE CAPTION FILTER: {USE_CAPTION_FILTER}
AUTO DELETE: {AUTO_DELETE}
SPELL CHECK: {SPELL_CHECK}
PROTECT CONTENT: {PROTECT_CONTENT}
"""

print(LOG_STR)
