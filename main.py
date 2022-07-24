import asyncio
import discord
from discord import colour
from discord.ext import commands
from discord import Embed
import sys


from lichessHelper import get_personnal_ranking, get_top_n_members

## Ce fichier contient l'implementation du bot discord, ainsi que toutes ces fonctoins

bot = commands.Bot(command_prefix='$',activity=discord.activity.Game("God-level Chess"))
@bot.event
async def on_ready():
    print("connected")
@bot.command(help="get ranking of one member")
async def ranking(ctx,username,category=""):
    embed = Embed(title = f"Ranking of {username}",colour = colour.Color.blue(),description="")
    for categoryName,rank in get_personnal_ranking(username,category):
        embed.add_field(name =categoryName,value=rank)
    await ctx.send(embed=embed)

bot.run("TOKEN PLACEMENT")
    