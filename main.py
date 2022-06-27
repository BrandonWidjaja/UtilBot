import discord
from discord.ext import commands
import requests
import random
import json
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
client = commands.Bot(command_prefix='!util ')
client.remove_command("help")
DISCORD_API = os.getenv("DISCORD_TOKEN")

# initialise


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=""))

client.run(DISCORD_API)
