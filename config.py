# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "28573904"))
API_HASH = os.environ.get("API_HASH", "928cc39b34ffd600217e9913571e2a7e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6386844628:AAFStmfJ7HFjv4qW5ahm__aY1GL0WnZJR2E")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1298057853")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "VenomOfficial")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://rehanmallick25300:#rehan@9080#@cluster0.q1ibcbl.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1298057853")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001843778389")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Everything For Free") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
