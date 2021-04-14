import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('Bot is ready');

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')
    
@client.event   
async def on_member_remove(member):
    print(f'{member} has left a server')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

    
    
#token
client.run('ODMxNzc3NzU5MTg0Mjg5Nzk5.YHaLZw.0svbfRRPa6ZLlw5LZPQ8GRHPDrU')