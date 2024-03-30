import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def calc(ctx, x = 0, z = "", y = 0):
    if z == "+":
        await ctx.send (x + y)
    elif z == "-":
        await ctx.send (x - y)
    elif z == "*":
        await ctx.send (x * y)
    elif z == ":" or z == "/":
        if y == 0:
            await ctx.send ("делить на 0 нельзя")
        else:
            await ctx.send (x / y)
    else:
        await ctx.send ("такого знака нет")
bot.run("MTIxOTMwNDMxODgyMjUxODc4NQ.GEykfF.V5VxEkNzE5TLxCxBhzfelWqs5uNdyD5JhxwJzg")
