import os

API_ID = int(os.environ.get("API_ID", 35935694))
API_HASH = os.environ.get("API_HASH", "270fc7395c68e32a907b0baaf910700c")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8678869575:AAGgF-LGcw0UP3d6YB3D7K3EaIqBcS5NhDs")

# Dùng duy nhất 1 đường dẫn này
REDIS_URL = os.environ.get("REDIS_URL", "redis://red-d8jli5sm0tmc73fej0jg:6379")

# Các biến này để tránh lỗi ImportError
HOST = ""
PORT = 0
PASSWORD = ""

PRIVATE_CHAT_ID = int(os.environ.get("PRIVATE_CHAT_ID", -1003998476130))
ADMINS = [int(x) for x in os.environ.get("ADMINS", "5575707907").split()]
