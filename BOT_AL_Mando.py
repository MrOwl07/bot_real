import discord
import os
from discord.ext import commands
from bot_logic import gen_pass
import random as r
import requests
import comand_api as c
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
async def pasw(ctx,a,b):
    nombre = str(a)
    await ctx.send(gen_pass(b)+nombre)
    
@bot.command(name="suma")
async def sumar(ctx,a,b):
    response = int(a) + int(b)
    await ctx.send(f"la suma es:{response}")

#Clese hoy
@bot.command(name = "meme")
async def mem(ctx):
    with open("Memes/juzgar.jpg","rb") as f:
        picture = discord.File(f)
    await ctx.send(file = picture)

#CLase de HOY
@bot.command(name = "momos")
async def momo(ctx):
    img_mem = r.choice(os.listdir("Memes"))
    with open(f"Memes/{img_mem}","rb") as f:
        picture = discord.File(f)
    await ctx.send(file = picture)
#CLase de HOY
@bot.command(name = "patos")
async def duck(ctx):
    image_url = c.get_duck_image()
    await ctx.send(image_url)
#CLase de HOY
@bot.command(name = "anime")
async def anime(ctx, a):
    query = a
    anime_data = c.get_anime_image(query)

    if anime_data:
        for anime in anime_data:
            
            image_url = anime['attributes']['posterImage']['small']

            await ctx.send(f"Image URL: {image_url}")
    else:
        await ctx.send("No se pudieron obtener datos de anime.")
bot.run(token)


