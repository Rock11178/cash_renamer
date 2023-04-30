import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6294701429:AAG4fRW8WuRDz4e1yl-QMyBIyOxDYyFBDxo")

API_ID = int(os.environ.get("API_ID", "25813158"))

API_HASH = os.environ.get("API_HASH", "339b4160cd59c680bc4e5b7cca61b9d5")

STRING = os.environ.get("STRING", "")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
