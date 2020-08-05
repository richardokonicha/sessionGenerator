import pymongo
import telebot
from dotenv import load_dotenv
import os
load_dotenv()

ckey = os.getenv("ckey")
csecret = os.getenv("csecret")
debug = (os.getenv("DEBUG") == 'True')
token = os.getenv("token")
url = os.getenv("url")
db_host = os.getenv("db_host")
api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")

bot = telebot.TeleBot(
    token,
    threaded=True
)

client = pymongo.MongoClient(db_host)
