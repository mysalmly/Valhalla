import discord
from discord.ext import commands
import os
import random 
import aiohttp
INTENTS = discord.Intents.default()
client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.Game, name =f"Valhalla || prefix = . "))
  

@client.command()
async def ping(ctx, self):
    await ctx.send(f"Pong! {round(self.client.latency * 1000)}ms")
  

@client.command()
async def meme(ctx):
        async with aiohttp.ClientSesssion() as cs:
            async with cs.get(
                    "https://www.reddit.com/r/REDDITSUB.json") as r:
                memes = await r.json()
                embed = discord.Embed(color=discord.Color.gray())
                embed.set_image(url=memes["data"]["children"][random.randit(
                    0, 100)]["data"]["url"])
                embed.set_footer(
                    text=f"Powered by r/REDDITSUB | meme requested by {ctx.author}"
                )
                await ctx.send(embed=embed)


client.run('TOKEN')
