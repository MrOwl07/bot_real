import discord
import os
from discord.ext import commands
from bot_logic import gen_pass
import random as r

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
token = "MTIzOTk4NTA5OTU4MDI0ODA4NA.GZ28rj.wd3y1ppa6vMLfxiqnzN0UpXMxGFH6wzaWyTdR8"
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command(name = "Password")
async def pasw(ctx,a):
    nombre = str(a)
    await ctx.send(gen_pass(20)+nombre)
    
@bot.command(name="suma")
async def sumar(ctx,a,b):
    response = int(a) + int(b)
    await ctx.send(f"la suma es:{response}")
    
@bot.command(name = "meme")
async def mem(ctx):
    with open("Memes/juzgar.jpg","rb") as f:
        picture = discord.File(f)
    await ctx.send(file = picture)
    
@bot.command(name = "momos")
async def momo(ctx):
    img_mem = r.choice(os.listdir("Memes"))
    with open(f"Memes/{img_mem}","rb") as f:
        picture = discord.File(f)
    await ctx.send(file = picture)

bot.run(token)

#creacion
