import discord
import os
from discord.ext import commands
from bot_logic import gen_pass
import random as r
import requests
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
token = "MTIzOTk4NTA5OTU4MDI0ODA4NA.GZ28rj.wd3y1ppa6vMLfxiqnzN0UpXMxGFH6wzaWyTdR8"

#funcion para la solicitud de api para imagenes de patos
def get_duck_image():
    url = 'https://random-d.uk/api/random'
    res =  requests.get(url)
    data = res.json()
    return data['url']
#funcion de consulta API am¿nime
def get_anime_image(query):
    url = ' https://kitsu.io/api/edge/anime'
    params = {
        'filter[text]' : query
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['data']
    else:
        print(f"Error: {response.status_code}")
        return None
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

@bot.command(name = "patos")
async def duck(ctx):
    image_url = get_duck_image()
    await ctx.send(image_url)

@bot.command(name = "anime")
async def anime(ctx, a):
    query = a
    anime_data = get_anime_image(query)

    if anime_data:
        for anime in anime_data:
            
            image_url = anime['attributes']['posterImage']['small']

            await ctx.send(f"Image URL: {image_url}")
    else:
        await ctx.send("No se pudieron obtener datos de anime.")
bot.run(token)


