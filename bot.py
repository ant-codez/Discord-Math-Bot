import discord
import random
import asyncio
import os
from discord.ext import commands
from equation_generator import EquationGenerator
from database import Database

client = commands.Bot(command_prefix = '$')
e_generator = EquationGenerator()
op_list = ["+", "*", "/", "-"]
db = Database()

@client.event
async def on_ready():
    print('Bot is ready')

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
    print(f"Sent by user id ={ctx.author.id} name = {ctx.author.name}")
    key = db.user_id_exists(ctx.author.id)
    if key == None: # user is not in database
        key = db.create_user(ctx.author.id, ctx.author.name)

    print(db.select_all())
    
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
            db.inc_correct(id)
            await ctx.send("Correct!")
        else:
            db.inc_incorrect(id)
            await ctx.send("Wrong! {}".format(e_generator.answer))

    await ctx.send("Score = {} to {}".format(db.get_correct(id), db.get_incorrect(id)))
    
    
    
#token
token = "ODMxNzc3NzU5MTg0Mjg5Nzk5.YHaLZw.hTdphipQluSQfWEe4gMr4aWEits"
#token = os.environ['DISCORD_TOKEN']
client.run(token)