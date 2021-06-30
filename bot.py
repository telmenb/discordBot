import os, discord, random
from discord.ext import commands
from dotenv import load_dotenv

# Retrieve token using dotenv
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Initialization of client
intent = discord.Intents(messages = True, reactions = True,\
     guilds = True, members = True, presences = True)
client = commands.Bot(command_prefix='!', intents=intent)

@client.event
async def on_ready():
    print(f"{client.user.name} has connected to Discord")

@client.event
async def on_member_join(member):
    guild = client.guilds[0]
    channel = discord.utils.get(guild.channels, name = "bottest")
    await channel.send(f"{member.name} ч гэнэ үү, {guild.name}-д тавтай морилно уу?\nХужаа л биш бол яахав")

@client.command(help="Creates an instant-invite link")
async def invite(ctx):
    link = await ctx.channel.create_invite(max_age = 0)
    await ctx.send(f"Here is an instant-invite link: {link}")

@client.command(help="Kicks a member from the guild")
async def kick(ctx, member: discord.Member, *, reason):
    await member.send(f"You have been kicked for: {reason}")
    await member.kick(reason = reason)

@client.command(help="Bans a member from the guild")
async def ban(ctx, member: discord.Member):
    await member.send(f"You have been banned for: {reason}")
    await member.ban()

@client.command(help="Unbans a user from the guild")
async def unban(ctx, name, *, reason):
    guild = client.guilds[0]
    bans = await guild.bans()
    user = None
    for tuuple in bans:
        if tuuple[1].name == name:
            user = tuuple[1]
            await guild.unban(user)
    return

@client.command(help="Sends a direct message to a member")
async def dm(ctx, member:discord.Member, *, msg:str):
    await member.send(msg)

client.run(TOKEN)
