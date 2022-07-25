import discord
from discord import colour
from discord.ext import commands
from discord import Embed


from lichessHelper import get_personnal_ranking, get_top_n_members

TOKEN = ""

# Ce fichier contient l'implementation du bot discord, ainsi que toutes ces fonctoins

bot = commands.Bot(command_prefix='$',
                   activity=discord.activity.Game("À votre service"))


@bot.event
async def on_ready():
    print("connected")


@bot.command(help="get ranking of one member")
async def ranking(ctx, username, category=""):
    embed = Embed(title=f"Ranking of {username}",
                  colour=colour.Color.blue(), description="")
    for categoryName, rank in get_personnal_ranking(username, category):
        embed.add_field(name=categoryName, value=rank)
    await ctx.send(embed=embed)


@bot.command(help="get top players")
async def top(ctx, n, category):
    embed = Embed(title=f"Top players in {category}",
                  colour=colour.Color.blue(), description="")
    for i, (rating, username) in enumerate(reversed(get_top_n_members(category, n))):
        embed.add_field(name=f"{i+1}.{username}", value=rating, inline=False)
    await ctx.send(embed=embed)

bot.run(TOKEN)
