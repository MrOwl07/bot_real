import discord
import os
from discord.ext import commands
import bot_logic as BL
import random as r
import requests
import comand_api as c
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
token = os.getenv("dt")


@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')
    
#comando para crear contraseña
@bot.command(name = "Password")
async def pasw(ctx,a:str,b:int):
    nombre = str(a)
    ctr = BL.gen_pass(b)
    await ctx.send(f"Su contraseña es: {ctr}{nombre}")

#comando para generar una suma de dos digitos
@bot.command(name="suma")
async def sumar(ctx,a:int,b:int):
    response = BL.suma(a,b)
    await ctx.send(f"la suma es:{response}")

#comando que rastrea una imagen dentro de una carpeta
@bot.command(name = "meme")
async def mem(ctx):
    with open("Memes/juzgar.jpg","rb") as f:
        picture = discord.File(f)
    await ctx.send(file = picture)

#Comando para arrojar un meme aleatorio desde la carpeta local
@bot.command(name = "momos")
async def momo(ctx):
    img_mem = r.choice(os.listdir("Memes"))
    with open(f"Memes/{img_mem}","rb") as f:
        picture = discord.File(f)
    await ctx.send(file = picture)
#Comando para activar API de img random de patos
@bot.command(name = "patos")
async def duck(ctx):
    image_url = c.get_duck_image()
    await ctx.send(image_url)
#Comando para activar API de img de anime por busqueda con palabra clave
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


