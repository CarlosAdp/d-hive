import os

from dotenv import load_dotenv
import discord

load_dotenv()


class HiveDJClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.lower().startswith('hey dj'):
            await message.channel.send(
                'Hey! What can I do for you? Differently from other DJs, you '
                'can ask me to play music, and I will play it for you!')


intents = discord.Intents.default()
intents.message_content = True

hive_dj_client = HiveDJClient(intents=intents)
hive_dj_client.run(os.getenv('DISCORD_BOT_TOKEN'))
