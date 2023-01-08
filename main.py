from telethon import TelegramClient, events, sync
from dotenv import load_dotenv
import os

load_dotenv()

api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")
phone = os.getenv("TELEGRAM_PHONE")

client = TelegramClient(phone, api_id, api_hash)
client.start()

# get new messages from
# channelslist = ["trade", "me"]
# and save them to jsom file
chanelist = ["trade", "me"]


@client.on(events.NewMessage(chats = chanelist))
async def handler(event):
    print("Event Occured")
    print(event.raw_text)
    print(event.message.to_dict())
    print(event.message.chat.id)
    print(event.message.chat.username)

client.start()
client.run_until_disconnected()

