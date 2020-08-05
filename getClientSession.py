from telethon.sync import TelegramClient
from telethon.tl.functions.messages import AddChatUserRequest, GetFullChatRequest, SendMessageRequest
from telethon.tl.functions.channels import JoinChannelRequest, InviteToChannelRequest
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from telethon.sessions import StringSession
from dotenv import load_dotenv
import os
import datetime


load_dotenv()
api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")
sessionString = os.getenv("sessionString")

client = TelegramClient(StringSession(), api_id, api_hash)

# client = TelegramClient(
#     StringSession(sessionString), api_id, api_hash)

# assert client.connect()


# client = TelegramClient(
#     'anon', 1347918, '5681581438678d9390cd4f67ee764f82')
# sessionString = StringSession.save(client.session)

# client = TelegramClient(
#     StringSession(sessionString), api_id, api_hash)

# if not client.is_user_authorized():
#     client.send_code_request(phone)
#     client.sign_in(phone, input("Enter code"))
# client = TelegramClient('client', api_id,  api_hash).start(bot__client_token='1261225499:AAFBWIrd2oCKH4FarmRl-w1R9tW2Q-xxG9E')

async def send_req(phone_number):
    # checks group if user is already participant
    # client = TelegramClient('anon', api_id, api_hash)
    await client.connect()
    authorized = await client.is_user_authorized()
    if not authorized:
        await client.send_code_request(phone_number)
        return None
    else:
        string = StringSession.save(client.session)
        return string
        


async def enter_req(phone_number, request_code):
    me = await client.sign_in(phone_number, request_code)
    authorized = await client.is_user_authorized()
    if authorized:
        string = StringSession.save(client.session)
        return string
    else:
        return None

async def get_phone(userid):
    contact = await client.get_entity(userid)
    pass

# client.get_me()
#     assert client.connect()
#     if not client.is_user_authorized():
#         client.send_code_request(phone_number)
#         me = client.sign_in(phone_number, input('Enter code: '))



    # channel = await client.get_entity(channel_name)
    # async for user in client.iter_participants(channel):
    #     if user_to_add == user.id:
    #         return True
    # return False


# client.loop.run_until_complete(get_phone())
