import os

from dotenv import load_dotenv
import discord

load_dotenv()

class HiveDJClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

intents = discord.Intents.default()
intents.message_content = True

hive_dj_client = HiveDJClient(intents=intents)
hive_dj_client.run(os.getenv("DISCORD_BOT_TOKEN"))
