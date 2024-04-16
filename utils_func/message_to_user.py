import configparser
from telethon import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest
import emoji

config = configparser.ConfigParser()
config.read('secret_data/config.ini')

API_ID = int(config['Telegram']['API_ID'])
API_HASH = config['Telegram']['API_HASH']

client = TelegramClient('anonimizer', API_ID, API_HASH)


async def get_user(username):

    user = await client(GetFullUserRequest(username))

    return user


async def main(text, username):

    await client.start()

    user = await get_user(username)
    user_id = user.full_user.id
    first_name = user.users[0].first_name

    await client.send_message(user_id, f'Здравствуй👋, <b>{first_name}</b>, '
                                       f'я <a href="https://www.google.com">AnonMessage</a>\n\n'
                                       f'Отправляю анонимные сообщения💬\n\n'
                                       f'Канал со всей информацией обо мне: @anonmessageofficial 👈\n\n'
                                       f'<i>made by <a href="@kolo_id">kolo</a></i>\n\n'
                                       f'<u>Тебе было отправлено сообщение👇</u>', parse_mode='html')

    await client.send_message(user_id, text)

    await client.disconnect()
