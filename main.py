import discord
from discord.ext import commands
from botLogic import flip_coin, gen_pass, gen_emoji

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def pwgen(ctx):
    password = gen_pass(10)  # Generate a 10-character password
    await ctx.send(f"Generated password: {password}")

@bot.command()
async def cflip(ctx):
    result = flip_coin()  # Flip a coin
    await ctx.send(f"The coin landed on: {result}")

@bot.command()
async def emoji(ctx):
    emoji = gen_emoji()  # Generate a random emoji
    await ctx.send(emoji)

@bot.command()
async def ten_emoji(ctx):
    emojis = [gen_emoji() for _ in range(10)]  # Generate a list of 10 random emojis
    await ctx.send(' '.join(emojis))

@bot.command()
async def heh(ctx, count: int = 5):
    await ctx.send("he" * count)

@bot.command()
async def lol(ctx, count: int = 5):
    await ctx.send("LO" * count)

bot.run("*** no ***")
