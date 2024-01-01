# API DISCORD
from discussion import *
import discord
from discord.ext import tasks, commands

# DATA STRUCTURES (arbre, hashMap, liste)
from data_structures.liste import chained_list
from data_structures.arbre import Discusion_tree
from discussion import Disscussion
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
discussion_on = False
disscussion = Disscussion

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
    global discussion_on, disscussion
    historique.append("help")
    await send(ctx,Disscussion,['✅','❌'])
    discussion_on = True
    userAnswer = await bot.wait_for("reaction_add")
    Disscussion.next_message(rightOrLeftReaction(userAnswer[0]))
    print(userAnswer[0])


@bot.command(name="exit")
async def exit(ctx):
    historique.append("exit")
    global discussion_on, disscussion
    discussion_on = False
    disscussion.goRoot()
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
async def on_reaction_add(reaction,user):
    global Disscussion
    if reaction.message.author != user:
        opt = rightOrLeftReaction(reaction)
        Disscussion.next_message(opt)
        print(f"Reaction : {reaction}")
        print(f"User : {user}")
        await send(reaction.message,Disscussion,['✅','❌'])
        
        
@bot.event
async def on_message(message):
    global path, data, historique, Disscussion, discussion_on
    discussion_on = discussion_on
    if message.author == bot.user:
        return
    else:
        path = "historique/" + str(message.author.id) + ".json"
        data = saveExist(path)
        if (historique.lenght() < 1):
            historique = saveImport(data)

        message.content = message.content.lower()

        print("discussion : ", discussion_on)
        if discussion_on and message.content!="!exit":
            if Disscussion.isLastMessage():
                discussion_on = False
                disscussion.goRoot()
                return
            else:
                
                await send(message,Disscussion,['✅','❌'])

                

    await bot.process_commands(message)
    


bot.run(os.getenv("BOT_ID"))

