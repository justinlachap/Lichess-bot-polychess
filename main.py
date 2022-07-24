import asyncio
import discord
from discord import colour
from discord import Embed
from discord.ext import commands
import sys

from lichessHelper import get_personnal_ranking, get_top_n_members

## Ce fichier contient l'implementation du bot discord, ainsi que toutes ces fonctoins

bot = commands.Bot(command_prefix='$',activity=discord.activity.Game("God-level Chess"))
@bot.event
async def on_ready():
    print("connected")
@bot.command(help="get ranking of one member")
async def ranking(ctx,username,category=""):
    embed = Embed(f"Ranking of {username}",colour.Color.blue(),"")
    for categoryName,rank in get_personnal_ranking(username,category):
        embed.add_field(categoryName,rank)
    await ctx.send(embed=embed)

if __name__ == "__main__":
    bot.run("TOKEN SHOOULD BE HERE")
        