import discord
from dotenv import load_dotenv
import os
import requests
import json

def get_meme():
    response = requests.get('https://meme-api.com/gimme')  # fetch a meme
    json_data = json.loads(response.text)
    return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')

        if message.content.startswith('$meme'):
            meme_url = get_meme()
            await message.channel.send(meme_url)

# Load token from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
