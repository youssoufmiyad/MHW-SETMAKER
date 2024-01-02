# API DISCORD
from discussion import *
import discord
from discord.ext import tasks, commands

# DATA STRUCTURES (arbre, hashMap, liste)
from data_structures.liste import chained_list
from data_structures.hashMap import avancement_conversation
from discussion import Disscussion
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
conversation = avancement_conversation
utilisateurs = []
messages = []
id = 0
botAnswer=""

################################ HISTORIQUE ##################################

# Suppression de l'historique


@bot.command(name="cls")
async def clear(ctx):
    global historique
    historique = chained_list()
    historique.append("cls")
    saveHistory(data, historique, file=open(path, "r+"))

# Visionnage de l'historique


@bot.command(name="historique")
async def history(ctx):
    global historique
    h = []
    for i in range(historique.lenght()):
        h.append(historique.get(i))
    await ctx.channel.send(h)
    historique.append("historique")
    saveHistory(data, historique, file=open(path, "r+"))

# Visionnage de la dernière commande saisie


@bot.command(name="last_command")
async def history_last(ctx):
    global historique
    await ctx.channel.send(historique.get(historique.lenght()-1))
    historique.append("last_command")
    saveHistory(data, historique, file=open(path, "r+"))

################################ DISCUSSION ##################################

# Lancement de la conversation


@bot.command(name="help")
async def help(ctx):
    global discussion_on, disscussion, dataConv, conversation, author_id, utilisateurs, messages,botAnswer
    dataConv = saveConversationExist()
    conversation = conversationsLoading(dataConv)
    utilisateurs = conversation.get("utilisateurs")
    messages = conversation.get("message")
    historique.append("help")
    botAnswer = await send(ctx, disscussion, ['✅', '❌'])
    discussion_on = True
    if len(utilisateurs) == 0:
        utilisateurs.append(author_id)
    for i in range(len(utilisateurs)):
        if utilisateurs[i] == author_id:
            id = i
            print(f"USER {utilisateurs[i]} ALREADY REGISTERED, ID : {id}")
        elif utilisateurs[i] != author_id and i == len(utilisateurs)-1:
            utilisateurs.append(author_id)
            print("NEW USER")
            id = len(utilisateurs)
    print(f"UTILISATEURS : {utilisateurs}, MESSAGES: {messages}")
    conversation.set("utilisateurs", utilisateurs)
    conversation.set("message", messages)
    saveConversations(dataConv, conversation, file=open(
        "historique/conversations.json", "r+"))


@bot.command(name="exit")
async def exit(ctx):
    historique.append("exit")
    global discussion_on, disscussion
    discussion_on = False
    disscussion.goRoot()


@bot.command(name="reset")
async def reset(ctx):
    historique.append("reset")
    global disscussion, discussion_on, messages, id, conversation
    disscussion.goRoot()
    messages[id] = []
    conversation.set("message", messages)
    saveConversations(dataConv, conversation, file=open(
        "historique/conversations.json", "r+"))
    if discussion_on:
        await send(ctx, disscussion, ['✅', '❌'])


@bot.command(name="speak_about")
async def speakAbout(ctx, subject=""):
    global discussion_on
    historique.append("speak_about")
    if subject == None or subject == "":
        await ctx.channel.send("Renseignez le sujet dont vous voulez savoir si je parle")
    elif subject in "Monster Hunter World Iceborne" or subject in "Monstres" or subject in "Equipement":
        await ctx.channel.send("Je peux vous aider à ce sujet, saisissez la commande !help puis demandez moi mes fonctionalités pour en savoir plus")
    else:
        await ctx.channel.send(f'Navré, je crains ne pas pouvoir vous aider au sujet de "{subject}"')
    discussion_on = False

##############################################################################


@bot.command(name="clear")
async def delete(ctx):
    historique.append("clear")
    saveHistory(data, historique, file=open(path, "r+"))
    ms = ctx.channel.history(limit=10)

    async for message in ms:
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
async def on_reaction_add(reaction, user):
    global disscussion, dataConv, utilisateurs, messages, id, conversation,botAnswer
    if reaction.message.author != user and reaction.message.id == botAnswer.id:
        opt = rightOrLeftReaction(reaction)
        disscussion.next_message(opt)
        if len(messages) <= id:
            messages.append(disscussion.get_path())
        else:
            messages[id] = disscussion.get_path()
        print(f"Reaction : {reaction}")
        print(f"User : {user}")
        botAnswer=await send(reaction.message, disscussion, ['✅', '❌'])
        conversation.set("utilisateurs", utilisateurs)
        conversation.set("message", messages)
        saveConversations(dataConv, conversation, open(
            "historique/conversations.json", "r+"))


@bot.event
async def on_message(message):
    global path, data, dataConv, historique, Disscussion, discussion_on, conversation, utilisateurs, messages, id, author_id, botAnswer
    discussion_on = discussion_on
    if message.author == bot.user:
        return
    elif "!speak_about" not in message.content.lower():
        author_id = str(message.author.id)
        path = "historique/" + author_id + ".json"
        data = saveHistoryExist(path)
        if (historique.lenght() < 1):
            historique = historyLoading(data)

        dataConv = saveConversationExist()
        conversation = conversationsLoading(dataConv)
        utilisateurs = conversation.get("utilisateurs")
        messages = conversation.get("message")

        message.content = message.content.lower()

        print("discussion : ", discussion_on)
        if discussion_on and message.content != "!exit":
            print(f"UTILISATEURS : {utilisateurs}, MESSAGES: {messages}")
            if Disscussion.isLastMessage():
                discussion_on = False
                disscussion.goRoot()
                messages[id] = []
                conversation.set("message", messages)
                saveConversations(dataConv, conversation, file=open(
                    "historique/conversations.json", "r+"))
                return
            elif message.content != "!reset":
                await send(message, Disscussion, ['✅', '❌'])

    await bot.process_commands(message)

bot.run(os.getenv("BOT_ID"))
