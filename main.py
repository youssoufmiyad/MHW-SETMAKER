#API DISCORD
import discord
from discord.ext import tasks, commands

#DATA STRUCTURES (arbre, hashMap, liste)
from data_structures.liste import chained_list
from datetime import datetime


#API Monster Hunter World
from API import *

#Variables .ENV
import os
from dotenv import load_dotenv
load_dotenv()

historique = chained_list()
now = datetime.now()

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents = intents)
client = discord.Client

@bot.command(name="clear")
async def delete(ctx):
  messages = ctx.channel.history(limit=10)

  async for message in messages:
    await message.delete()
    print("deleted")
  
@bot.command(name="hist")
async def history(ctx):
  if os.path.isfile(str(ctx.message.author.id)+".json"):
    print("user "+str(ctx.message.author.id)+" has a save file")
  else:
    print("user "+str(ctx.message.author.id)+" doesnt have a save file")
    

@bot.event
async def on_ready():
    print("Le bot est prêt !")

@bot.event
async def on_member_join(member):
    general_channel = bot.get_channel(1167470031345553502)
    await general_channel.send("Bienvenue sur le serveur ! "+ member.name)

@bot.event
async def on_message(message):

  if message.author == bot.user:
    return

  message.content = message.content.lower()

  if message.content.startswith("hello"):
    await message.channel.send("Hello "+message.author.display_name)

  await bot.process_commands(message)


bot.run(os.getenv("BOT_ID"))