import discord
from discord.ext import commands
PREFIX = '.'
INTENTS = discord.Intents.default()
client = discord.Client(commands_prefix=PREFIX, intents=INTENTS)

class Status(commands.Cog):
  def __init__(self, client):
    self.client = client


  async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"Your servers"))


def setup(client):
    client.add_cog(Status(client))