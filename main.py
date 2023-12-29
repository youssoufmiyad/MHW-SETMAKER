# API DISCORD
from discussion import *
import discord
from discord.ext import tasks, commands

# DATA STRUCTURES (arbre, hashMap, liste)
from data_structures.liste import chained_list
from data_structures.arbre import Discusion_tree
from datetime import datetime
from utils import *

# API Monster Hunter World
from API import *

# Variables .ENV
import os
from dotenv import load_dotenv
load_dotenv()

# API Discord
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)
client = discord.Client

# Variables de l'historique
historique = chained_list()
path = ""

# Variables de la discussion avec le bot
discussion = Discusion_tree()
discussion.add_first_message(FIRST_MESSAGE)

################################ HISTORIQUE ##################################

# Suppression de l'historique


@bot.command(name="cls")
async def clear(ctx):
    historique = chained_list()
    saveExport(data, historique, file=open(path, "r+"))

# Visionnage de l'historique


@bot.command(name="hist")
async def history(ctx):
    h = ""
    for i in range(historique.lenght()):
        h += '"'+historique.get(i)+'"\n'
    print(h)
    historique.append("hist")
    saveExport(data, historique, file=open(path, "r+"))

#############################################################################

################################ DISCUSSION ##################################

# Lancement de la conversation


@bot.command(name="help")
async def help(ctx):
    print(discussion.show_message())

##############################################################################


@bot.command(name="clear")
async def delete(ctx):
    historique.append("clear")
    saveExport(data, historique, file=open(path, "r+"))
    messages = ctx.channel.history(limit=10)

    async for message in messages:
        await message.delete()
        print("deleted")


@bot.event
async def on_ready():
    print("Le bot est prêt !")


@bot.event
async def on_member_join(member):
    general_channel = bot.get_channel(1167470031345553502)
    await general_channel.send("Bienvenue sur le serveur ! " + member.name)


@bot.event
async def on_message(message):
    global path
    global data
    global historique
    global discussion
    if message.author == bot.user:
        return
    path = "historique/" + str(message.author.id) + ".json"
    data = saveExist(path)
    if (historique.lenght() < 1):
        historique = saveImport(data)

    await message.channel.send("resp")

    message.content = message.content.lower()

    if message.content.startswith("hello"):
        await message.channel.send("Hello "+message.author.display_name)

    await bot.process_commands(message)


bot.run(os.getenv("BOT_ID"))
