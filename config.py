import os

class Config(object):
    BOT_TOKEN = os.environ.get("6234022831:AAHCvRy6__wwXXhqnDB0R7sBo6R5SBjir1s")
    API_ID = int(os.environ.get("24250238"))
    API_HASH = os.environ.get("cb3f118ce5553dc140127647edcf3720")
    VIP_USER = os.environ.get('VIP_USERS', '').split(',')
    VIP_USERS = [int(8172163893) for user_id in VIP_USER]
