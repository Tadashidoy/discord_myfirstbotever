import discord
from discord.ext import commands
import random

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$yes'):
        await message.channel.send("of course") 
    elif message.content.startswith('$password'): 
        contrasenna=gen_pass(10)
        await message.channel.send(contrasenna)
    elif message.content.startswith('$bye'):
        await message.channel.send("see ya")
    else:
        await message.channel.send(message.content)

def gen_pass(pass_lenght):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_lenght):
        password += random.choice(elements)

    return password

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: float, right: float):
    await ctx.send(left + right)

@bot.command()
async def substract(ctx, left: float, right: float):
    await ctx.send(left - right)

@bot.command()
async def multiply(ctx, left: float, right: float):
    await ctx.send(left * right)

@bot.command()
async def divide(ctx, left: float, right: float):
    await ctx.send(left / right)

@bot.command()
async def cointoss(ctx):
    numero=random.randint(1,2)
    if numero==1:
        moneda="¡cara!"
    else:
        moneda="¡cruz!"
    await ctx.send(moneda)
bot.run()
