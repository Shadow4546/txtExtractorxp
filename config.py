#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7151674132:AAEZXSIktkinA3ZhzyEIqVZ6FuJgM2eMBM4")
    API_ID = int(os.environ.get("API_ID", "28935416"))
    API_HASH = os.environ.get("API_HASH", "e18c05697d95edfe39d8957f6e110308")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7170328188")
