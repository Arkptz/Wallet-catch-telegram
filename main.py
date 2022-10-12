# - *- coding: utf- 8 - *-
from telethon import TelegramClient, events, sync
import re, pickle, asyncio
import config as cfg
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
api_id = cfg.api_id
api_hash = cfg.api_hash
regex = r"wallet?start="
cheki = []
sexy = []
valid = []
kd = 0.0
client = TelegramClient('session', api_id, api_hash)
print(f'Enabled [Yes]')

@client.on(events.NewMessage([-1001778752731, -1001759984051]))
async def normal_handler(event):
    try:
        user_mess = event.message.to_dict()['reply_markup']['rows'][0]['buttons'][0]['url'][20:].split('=')
        await client.send_message('wallet', '/start '+user_mess[1])
        print('\n\n\n\n САССАААААТТТ \n\n\n\n')
        print(event.message.to_dict())
    except:
        print(event.message.to_dict())
        pass

client.start()
client.run_until_disconnected()
print('Выключение\n3...\n2...\n1...')