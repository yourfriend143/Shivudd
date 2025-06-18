#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29796588"))
API_HASH = environ.get("API_HASH", "f5385bda6aea1e012b4983e243b9481f")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "7795248617"))
CREDIT = "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎"
AUTH_USER = os.environ.get('AUTH_USERS', '7795248617').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
