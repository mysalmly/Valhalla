import discord
from discord.ext import commands
PREFIX = '.'
INTENTS = discord.Intents.default()
bot = discord.Client(commands_prefix=PREFIX, intents=INTENTS)

class Status(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"Your servers"))


def setup(bot):
    bot.add_cog(Status(bot))