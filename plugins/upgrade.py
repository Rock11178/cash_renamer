"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 30  ind /🌎 0.8$  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price Rs 60 ind /🌎 1.2$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price Rs 100  ind /🌎 2.5$  per Month
	
	Google play reedem code ```Buy Code```
	
	After Buy Code Send The Code To Me
        Payment To Admin @Sharathitsisme
        
    Premium Features
    💲 Rename Upto 4GB Files
    💲 Renaming Speed Averages - 10mbbs """
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Sharathitsisme")], 
        			[InlineKeyboardButton("updates",url = "https://t.me/Tamilan_Botsz"),
        			InlineKeyboardButton("Support",url = "https://t.me/TamilanBotsZ_Support")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 30  ind /🌎 0.8$  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price Rs 60  ind /🌎 1.2$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price Rs 100  ind /🌎 2.5$  per Month
	
	
	Google play reedem code ```Buy Code```
	
	After Buy Code Send The Code To Me
        Payment To Admin @Sharathitsisme
        
    Premium Features
    💲 Rename Upto 4GB Files
    💲 Renaming Speed Averages - 10mbbs """
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/mRiDerDM")], 
        			[InlineKeyboardButton("Updates",url = "https://t.me/Tamilan_BotsZ "),
        			InlineKeyboardButton("Support",url = "https://t.me/TamilanBotsZ_Support")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
