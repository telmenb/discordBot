from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')

@bot.command(name="idea", help="Get a random project idea")
async def idea(ctx):
    await ctx.send("Ideas are hard")
    await ctx.send("Don't worry, you're gonna be fine lol")

    topics = ['chat bot', 'cli', 'game', 'web bot']
    areas = ['pet care', 'doing homework']

    idea = f'Create a new {random.choice(topics)} that helps with {random.choice(areas)}'
    await ctx.send(idea)

@bot.command(name="calc", help="Do a two number calculation")
async def calc(ctx, x: float, fn, y: float):
    if fn == '+':
        await ctx.send(x + y)
    elif fn == '-':
        await ctx.send(x - y)
    elif fn == '*':
        await ctx.send(x * y)
    elif fn == '/':
        await ctx.send(x / y)

with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)
