import discord
from discord.ext import commands
import random, os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello! I am {bot.user}, a Discord chat bot!')

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):

    number = random.randint(1, 100)

    if number <= 60:
        filename = "mem1.webp"
        rarity = "Common"

    elif number <= 90:
        filename = "mem2.webp"
        rarity = "Rare"

    else:
        filename = "mem3.webp"
        rarity = "Legendary"

    picture = discord.File(f"images/{filename}")

    await ctx.send(f"🎲 Rarity: **{rarity}**", file=picture)

bot.run("MTU1MDE1NTI2ODQzMDQ5OTkzMQ.GMjFHy.ixEFd1A6ts4L6MOPZTqHl78xOey0qugkNi2ZtA")
