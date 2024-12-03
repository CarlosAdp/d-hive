import os
from typing import Literal, Optional

from dotenv import load_dotenv
from discord import app_commands
import discord

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f'Logged on as {client.user}!')
    await tree.sync()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('hey dj'):
        await message.channel.send(
            'Hey! What can I do for you? Differently from other DJs, you '
            'can ask me to play music, and I will play it for you!')

@tree.command(name='join', description='Join the D-Hive')
async def join(interaction: discord.Interaction):
    await interaction.response.send_message(
        'Welcome to the Hive DJ Party!',
        ephemeral=True,
        view=discord.ui.view.View(timeout=5)
    )

@tree.command(name='leave', description='Leave the D-Hive')
@app_commands.describe(
    where='Where do you want to leave (default: this server only)?')
async def leave(
    interaction: discord.Interaction,
    where: Optional[Literal['This server', 'All servers']] = None):
    await interaction.response.send_message(
        f'Leaving the Hive DJ Party{
            " on all servers!" if where == 'All servers' 
            else " on this server only"
        }'
    )


client.run(os.getenv('DISCORD_BOT_TOKEN'))
