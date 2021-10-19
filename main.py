import discord
from discord.ext import commands
from discord.ext
import os
PREFIX = '.'
INTENTS = discord.Intents.default()
client = discord.Client(commands_prefix=PREFIX, intents=INTENTS)


@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')

@client.command()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')

for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODk5NzMzMzY2MzI3MzQ1MTgy.YW3D_g.rkzoA31nHEeFgWArayZ66XcKfS0')