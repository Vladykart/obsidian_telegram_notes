from telethon import TelegramClient, events, sync
from settings import MONGO_CREDENTIALS as MG
from settings import TELEGRAM_CREDENTIALS as TG

phone = TG["phone"]
api_id = TG["api_id"]
api_hash = TG["api_hash"]

client = TelegramClient(phone, api_id, api_hash)
client.start()
channels = ["trade", "me"]


def get_all_messages(chanel):
    messages = client.get_messages(chanel, limit=None)
    message_list = []
    for message in messages:
        message_list.append(message.to_dict())
    return message_list


client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage(chats = channels))
async def handler(event):
    print("Event Occured")
    print(event.raw_text)
    print(event.message.to_dict())
    print(event.message.chat.id)
    print(event.message.chat.title)
    print(event.message.chat.username)

client.start()
client.run_until_disconnected()


