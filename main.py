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
