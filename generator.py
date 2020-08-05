from config import bot
import re
import database as db
from telethon.sync import TelegramClient
import re
from config import (token, debug, url, bot, api_id, api_hash)
import os


from getClientSession import send_req, client, enter_req, get_phone


def recieved_code(message, phone_number):
    userid = message.from_user.id
    request_code = message.text
    if re.match("code[0-9]+",request_code):
        request_code = request_code.strip("code")
        request_code = int(request_code)
        string = client.loop.run_until_complete(enter_req(phone_number, request_code))
        print(string)
        bot.send_message(userid, text=f"Here is your session <pre>{string}</pre>", parse_mode="html")
    else:
        msg = bot.send_message(userid, text="Please enter Login code you just recieved in correct format")
        bot.register_for_reply(msg, recieved_code, (phone_number))
    
    pass

def recieved_phone(message):
    userid = message.from_user.id
    phone_number = message.text
    if re.match(r"\+[0-9]+", phone_number):
        string_req = client.loop.run_until_complete(send_req(phone_number))
        if string_req:
            bot.send_message(userid, text=f"Here is your session <pre>{string_req}</pre>", parse_mode="html")
        else:
            msg = bot.send_message(userid, text="Please enter Login code you just recieved in this format <b>code12345</b>", parse_mode="html")
            bot.register_for_reply(msg, recieved_code, (phone_number))
    else:
        phone_req = bot.send_message(userid, text="Please enter phone number in the correct format")
        bot.register_for_reply(phone_req, recieved_phone)


@bot.message_handler(commands=["generate", "Generate"])
def generate(message):
    userid = message.from_user.id
    
    # phone_number = '+2349050556321'
    phone_req = bot.send_message(userid, text="Please enter your phone number")
    bot.register_for_reply(phone_req, recieved_phone)
    # bot.register_next_step_handler(phone_req, recieved_phone)


    # client.send_code_request(phone_number)
    # myself = client.sign_in(phone_number, input('Enter code: '))
    # If .sign_in raises PhoneNumberUnoccupiedError, use .sign_up instead
    # If .sign_in raises SessionPasswordNeeded error, call .sign_in(password=...)
    # You can import both exceptions from telethon.errors.


    pass