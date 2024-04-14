import configparser
from telethon import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest

config = configparser.ConfigParser()
config.read('config.ini')

API_ID = int(config['Telegram']['API_ID'])
API_HASH = config['Telegram']['API_HASH']

client = TelegramClient('kolo_id', API_ID, API_HASH)


async def get_user(username):

    user = await client(GetFullUserRequest(username))

    return user


async def main(text, username):

    await client.start()

    user = await get_user(username)
    user_id = user.full_user.id

    await client.send_message(user_id, text)

    await client.disconnect()
