import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('Bot is ready');

#token
client.run('ODMxNzc3NzU5MTg0Mjg5Nzk5.YHaLZw.0FI4k_C9RS4ckO1Ir2jKxwJaY5g')