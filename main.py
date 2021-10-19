import discord
from discord.ext import commands
import os
PREFIX = '.'
INTENTS = discord.Intents.default()
bot = discord.Client(commands_prefix=PREFIX, intents=INTENTS)


@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')

@bot.command()
async def load(ctx, extension):
  bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
  bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('ODk5NzMzMzY2MzI3MzQ1MTgy.YW3D_g.rkzoA31nHEeFgWArayZ66XcKfS0')