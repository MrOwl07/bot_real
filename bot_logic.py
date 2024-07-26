import random as r
import string
import os, discord
def gen_pass(pass_length):
    elements = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(pass_length):
        password += r.choice(elements)

    return password

def suma(a,b):
    return a+b

def meminos():
    img_mem = r.choice(os.listdir("Memes"))
    
    with open(f"Memes/{img_mem}","rb") as f:
        picture = discord.File(f)
        
    return picture