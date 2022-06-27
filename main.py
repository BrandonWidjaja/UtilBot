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

    async with channel.typing():

        embed = discord.Embed(title=f"Astronomy Picture of the Day: \n{json_data['title']}",
                              color=ctx.guild.me.top_role.color,
                              timestamp=ctx.message.created_at,)

        embed.add_field(
            name="Date Taken", value=f"**{json_data['date']}**", inline=False)
        embed.set_image(url=json_data['hdurl'])
        embed.add_field(
            name="HD Image:", value=f"**{json_data['hdurl']}**", inline=False)
        embed.set_footer(
            text=f"Requested by {ctx.author.name}")

    await channel.send(embed=embed)


@client.command(pass_context=True)
async def help(ctx):

    channel = ctx.message.channel
    seperator = '-------------------------------------------\n'

    embed = discord.Embed(title=f"Commands",
                          color=discord.Color.purple(),
                          timestamp=ctx.message.created_at,)

    embed.add_field(name=f'{seperator}ping',
                    value='Returns ping of the bot\n**Usage**: !util ping', inline=False)
    embed.add_field(name=f'{seperator}apod',
                    value='Returns NASA\'s Astrology Picture of the Day\n**Usage**: !util apod', inline=False)

    embed.set_footer(
        text=f"Requested by {ctx.author.name}")

    await channel.send(embed=embed)

client.run(DISCORD_API)
