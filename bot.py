import os, discord, random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

intent = discord.Intents(messages = True, reactions = True,\
     guilds = True, members = True, presences = True)
client = commands.Bot(command_prefix = '!', intents = intent)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord')

@client.event
async def on_member_join(member):
    guild = discord.utils.get(client.guilds, name = "Orc Pride")
    channel = discord.utils.get(guild.channels, name = "orc-saloon")
    await channel.send(f"{member.name} ч гэнэ үү, {guild.name}-д тавтай морилно уу?\nХужаа л биш бол яахав")


@client.command()
async def invite(ctx):
    link = await ctx.channel.create_invite(max_age = 0)
    await ctx.send(f"Here is an instant-invite link: {link}")

@client.command(aliases = ['8ball'], help = "Ask a question into the virtual 8ball")
async def _8ball(ctx, *, question):
    responses = ["It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes, definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most Likely",
        "Outlook Good",
        "Yes",
        "Signs point to yes",
        "Reply hazy, try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good", 
        "Very Doubtful"]
    
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

@client.command()
async def kick(ctx, member: discord.Member, *, reason = None):
    await member.kick(reason = reason)

client.run(TOKEN)
