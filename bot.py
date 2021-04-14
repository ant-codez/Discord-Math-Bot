import discord
import random
import asyncio
import os
from discord.ext import commands
from equation_generator import EquationGenerator

client = commands.Bot(command_prefix = '$')
e_generator = EquationGenerator()
op_list = ["+", "*", "/", "-"]

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

#seperates input by whitespace
@client.command()
async def math(ctx):
    print(f"Sent by user {ctx.author.id}")
    q = e_generator.generate(op_list[random.randint(0, len(op_list) - 1)])
    await ctx.send(q)
    
    def check(m):
        return m.author.id == ctx.author.id
    
    try:
        message = await client.wait_for('message', check = check, timeout=10.0)
    except asyncio.TimeoutError:
        await ctx.send("Sorry Times up!!")
    
    if message:
        if e_generator.check_answer(message.content):
            await ctx.send("Correct!")
        else:
            await ctx.send("Wrong! {}".format(e_generator.answer))
    
    
    
#token
token = os.environ['DISCORD_TOKEN']
client.run(token)