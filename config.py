# Copyright (C) 2021 By VideoStreamVCG

import os
from os import path, getenv
from dotenv import load_dotenv

if path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()

class Cyber(object):
        admins = {}
        BOT_TOKEN = getenv("BOT_TOKEN", 2115296273:AAFXymBgqIQDxfcy1sZjivKmEZL1tYKal4U)
        CHANNEL = int(os.getenv('CHANNEL', 123456))
        API_ID = int(getenv("API_ID", "13617023"))
        API_HASH = getenv("API_HASH", "e1aee21f08add5aa3132f092d4be1db5")
        SESSION_NAME = getenv("SESSION_NAME", BQCUEacdpTT8MAWP0gczCucrm6tWnCfWRg24LGhN6WXaUbVbXSZyV-haVKO_R6bhXIRspg9B3VtSow-pNuz16JJbuMs0cEDRB2YqojwmNWFueJFUbeR2hnPI592rDV4jVFFQzatx8ytjImBAWAVx0KzvX7DxUHyc11GUY9GkeWAzgoihG14SINKTEzRq1faiwzaFdPBJ3U4Mmz7uSIqfJpGJkGRcgFclrsNhB7XFQ8M-gMU7BgsMA_YYfQnrUuVQDTliPnqoilTDq5_U5815IrhzHSSi47uL14ujXG07JIZ2bYd2aYHsZiRGc7rJrCTWQKrePzLaiyrO5LDDgPh9duwefHZ59wA)
        DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
        SUDO_USERS = list(map(int, getenv("SUDO_USERS").split(1843424732)))
        ASSISTANT_NAME = getenv("ASSISTANT_NAME", "kukubot11")
        BOT_USERNAME = getenv("BOT_USERNAME", "kukuvc_bot")
        COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
        CHANNEL_NAME = getenv("CHANNEL_NAME", "PP")
        GROUP_NAME = getenv("GROUP_NAME", "MK")
        OWNER_NAME = getenv("OWNER_NAME", "𝙼𝚎𝚖𝚘𝚛𝚒𝚎𝚜-x")
