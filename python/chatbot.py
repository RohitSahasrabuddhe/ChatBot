# -*- coding: utf-8 -*-
from chatterbot import ChatBot


# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database="./database.sqlite3"
)

print("Type something to begin...")
response = bot.get_response("repair")
print(response)