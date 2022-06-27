from pydoc import cli
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

# ping command


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

NASA_API = os.getenv("NASA_KEY")


@client.command()
async def apod(ctx):

    response = requests.get(
        "https://api.nasa.gov/planetary/apod?api_key=" + NASA_API)
    json_data = json.loads(response.text)
    channel = ctx.message.channel

    await ctx.send(json_data)


client.run(DISCORD_API)
