import os, discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
GUILD = os.getenv('GUILD_NAME')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

@client.event
async def on_member_join(member):
    print("new member")
    await member.create_dm()
    await member.dm_channel.send(f'Hello {member.name}, Welcome to Orc Pride!')

client.run(TOKEN)
