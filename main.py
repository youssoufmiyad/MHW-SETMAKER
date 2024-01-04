# API DISCORD
from discussion import *
import discord
from discord.ext import tasks, commands

# DATA STRUCTURES (arbre, hashMap, liste)
from data_structures.liste import chained_list
from data_structures.hashMap import avancement_conversation
from discussion import Disscussion
from utils.historiqueComand import *
from utils.historiqueDiscussion import *
from utils.reponse import *
from utils.sets import *
from utils.element import elementEmoji

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
botAnswer = ""

sets = []

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
    for j in range(len(h)):
        await ctx.channel.send(h[len(h)-(1+j)])
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
    global discussion_on, disscussion, dataConv, conversation, author_id, utilisateurs, messages, botAnswer

    dataConv = saveConversationExist()
    conversation = conversationsLoading(dataConv)
    utilisateurs = conversation.get("utilisateurs")
    messages = conversation.get("message")

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

    conversation.set("utilisateurs", utilisateurs)
    conversation.set("message", messages)
    saveConversations(dataConv, conversation, file=open(
        "historique/conversations.json", "r+"))

    print("MESSAGE ID : ", messages)
    for option in messages[id]:
        disscussion.next_message(option)

    botAnswer = await send(ctx, disscussion)
    await botAnswer.add_reaction('✅')
    await botAnswer.add_reaction('❌')

    historique.append("help")
    saveHistory(data, historique, file=open(path, "r+"))

    print(f"UTILISATEURS : {utilisateurs}, MESSAGES: {messages}")

# Sortie de la conversation


@bot.command(name="exit")
async def exit(ctx):
    global discussion_on, disscussion
    discussion_on = False
    disscussion.goRoot()
    historique.append("exit")
    saveHistory(data, historique, file=open(path, "r+"))


# Retour à la première question


@bot.command(name="reset")
async def reset(ctx):
    global disscussion, discussion_on, messages, id, conversation, data, historique

    disscussion.goRoot()
    conversation.set("message", messages)
    messages[id] = []
    saveConversations(dataConv, conversation, file=open(
        "historique/conversations.json", "r+"))

    if discussion_on:
        botAnswer = await send(ctx, disscussion)
        await botAnswer.add_reaction('✅')
        await botAnswer.add_reaction('❌')

    historique.append("reset")
    saveHistory(data, historique, file=open(path, "r+"))


# Savoir si le bot traite d'un certain sujet (réponse négatives pour tout ce qui ne parle pas de MHW)


@bot.command(name="speak_about")
async def speakAbout(ctx, subject=""):
    global discussion_on
    if subject == None or subject == "":
        await ctx.channel.send("Renseignez le sujet dont vous voulez savoir si je parle")
    elif subject in "Monster Hunter World Iceborne" or subject in "Monstres" or subject in "Equipement":
        await ctx.channel.send("Je peux vous aider à ce sujet, saisissez la commande !help puis demandez moi mes fonctionalités pour en savoir plus")
    else:
        await ctx.channel.send(f'Navré, je crains ne pas pouvoir vous aider au sujet de "{subject}"')
    discussion_on = False
    historique.append("speak_about")
    saveHistory(data, historique, file=open(path, "r+"))


# Réponse en réaction


@bot.event
async def on_reaction_add(reaction, user):
    global disscussion, discussion_on, dataConv, utilisateurs, messages, id, conversation, botAnswer
    react = []
    if reaction.message.author != user and reaction.message.id == botAnswer.id:

        opt = rightOrLeftReaction(reaction)
        if len(messages) <= id:
            messages.append(disscussion.get_path())
        else:
            messages[id] = disscussion.get_path()
        print(f"Reaction : {reaction}")
        print(f"User : {user}")
        if disscussion.isLastMessage() == False:
            react.append('✅')
            react.append('❌')
            conversation.set("utilisateurs", utilisateurs)
            conversation.set("message", messages)
            saveConversations(dataConv, conversation, open(
                "historique/conversations.json", "r+"))

        else:
            disscussion.goRoot()
            messages[id] = []
            conversation.set("message", messages)
            saveConversations(dataConv, conversation, open(
                "historique/conversations.json", "r+"))
            discussion_on = False

        botAnswer = await send(reaction.message, disscussion)
        for r in react:
            await botAnswer.add_reaction(r)
        disscussion.next_message(opt)

        print(f"UTILISATEURS : {utilisateurs}, MESSAGES: {messages}")

################################ FONCTION PRINCIPALES ################################

# Lance la création d'un nouveau set


@bot.command(name="new_set")
async def new_set(ctx):
    return

# Montre à l'utilisateur tout ses sets


@bot.command(name="get_sets")
async def get_sets(ctx):
    global sets
    historique.append("get_sets")
    saveHistory(data, historique, file=open(path, "r+"))
    nb=1
    for s in sets:
        await ctx.send(f"SET {nb}")
        embedArmor = discord.Embed()
        embedArmor.add_field(name="ARMOR", value=s.armor.name, inline=False)
        await ctx.send(embed=embedArmor)
        
        for i in range(len(s.armor.pieces)):
            embedPiece =discord.Embed()
            embedPiece.add_field(name=s.armor.pieces[i]["type"], value=s.armor.pieces[i]["name"], inline=False)
            embedPiece.set_image(url=s.armor.pieces[i]["assets"]["imageMale"])
            await ctx.send(embed=embedPiece)
        
        embedWeapon = discord.Embed()
        embedWeapon.add_field(name="WEAPON", value=s.weapon.name+elementEmoji(s.weapon), inline=False)
        embedWeapon.set_image(url=s.weapon.assets["icon"])
        await ctx.send(embed=embedWeapon)
        nb+=1


################################ BOT ################################

# Suppression des messages (10 messages)


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

# Accueil nouveau membre


@bot.event
async def on_member_join(member):
    general_channel = bot.get_channel(1167470031345553502)
    await general_channel.send("Bienvenue sur le serveur ! " + member.name)


@bot.event
async def on_message(message):
    global path, data, dataConv, historique, Disscussion, discussion_on, conversation, utilisateurs, messages, id, author_id, botAnswer, sets
    message.content = message.content.lower()

    if message.author == bot.user:
        return
    elif "!speak_about" not in message.content:

        # Historique de commandes
        author_id = str(message.author.id)
        path = "historique/" + author_id + ".json"
        data = saveHistoryExist(path)
        sets = setsLoading(data)
        if (historique.lenght() < 1):
            historique = historyLoading(data)

        # ChatBot
        dataConv = saveConversationExist()
        conversation = conversationsLoading(dataConv)
        utilisateurs = conversation.get("utilisateurs")
        messages = conversation.get("message")

        print("discussion : ", discussion_on)
        if discussion_on and message.content != "!exit":

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
