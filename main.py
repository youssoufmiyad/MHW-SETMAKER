# API DISCORD
from discussion import *
import discord
from discord.ext import tasks, commands
from buttons import *
from selects import *

# DATA STRUCTURES (arbre, hashMap, liste)
from data_structures.liste import chained_list
from data_structures.hashMap import avancement_conversation
from discussion import *
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

# ANCHOR - historique
################################ HISTORIQUE ##################################

# Suppression de l'historique

# ANCHOR - !cls


@bot.command(name="history_clear")
async def clear(ctx):
    global historique
    historique = chained_list()
    historique.append("!cls")
    saveHistory(data, historique, file=open(path, "r+"))

# Visionnage de l'historique

# ANCHOR - !historique


@bot.command(name="historique")
async def history(ctx):
    global historique
    h = []
    for i in range(historique.lenght()):
        h.append(historique.get(i))
    for j in range(len(h)):
        await ctx.channel.send(h[len(h)-(1+j)])
    historique.append("!historique")
    saveHistory(data, historique, file=open(path, "r+"))

# Visionnage de la dernière commande saisie

# ANCHOR - !last_command


@bot.command(name="last_command")
async def history_last(ctx):
    global historique
    await ctx.channel.send(historique.get(historique.lenght()-1))
    historique.append("!last_command")
    saveHistory(data, historique, file=open(path, "r+"))

# ANCHOR - Discussion
################################ DISCUSSION ##################################

# Lancement de la conversation

# ANCHOR - !help


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

    match disscussion.show_message():
        case Messages.FIRST_MESSAGE:
            await botAnswer.add_reaction("⌨️")
            await botAnswer.add_reaction("🇫")
        case Messages.R | Messages.RL | Messages.RR:
            print("R")
            await botAnswer.add_reaction('✅')
            await botAnswer.add_reaction('❌')
        case Messages.RRR | Messages.RLR:
            await botAnswer.add_reaction('🐉')
            await botAnswer.add_reaction('<:greatsword:1191087208581574726>')

    historique.append("!help")
    saveHistory(data, historique, file=open(path, "r+"))

    print(f"UTILISATEURS : {utilisateurs}, MESSAGES: {messages}")

# Sortie de la conversation

# ANCHOR - !exit


@bot.command(name="exit")
async def exit(ctx):
    global discussion_on, disscussion
    discussion_on = False
    disscussion.goRoot()
    historique.append("!exit")
    saveHistory(data, historique, file=open(path, "r+"))


# Retour à la première question

# ANCHOR - !reset
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
        match disscussion.show_message():
            case Messages.FIRST_MESSAGE:
                await botAnswer.add_reaction("⌨️")
                await botAnswer.add_reaction("🇫")
            case Messages.R | Messages.RL | Messages.RR:
                await botAnswer.add_reaction('✅')
                await botAnswer.add_reaction('❌')
            case Messages.RRR | Messages.RLR:
                await botAnswer.add_reaction('🐉')
                await botAnswer.add_reaction('<:greatsword:1191087208581574726>')

    historique.append("!reset")
    saveHistory(data, historique, file=open(path, "r+"))


# Savoir si le bot traite d'un certain sujet (réponse négatives pour tout ce qui ne parle pas de MHW)

# ANCHOR - !speak_about
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
    historique.append("!speak_about")
    saveHistory(data, historique, file=open(path, "r+"))


# Réponse en réaction

# ANCHOR - on_reaction_add
@bot.event
async def on_reaction_add(reaction, user):
    global disscussion, discussion_on, dataConv, utilisateurs, messages, id, conversation, botAnswer
    if reaction.message.author != user and reaction.message.id == botAnswer.id:

        opt = rightOrLeftReaction(reaction)
        print(f"OPT = {opt}")
        if len(messages) <= id:
            messages.append(disscussion.get_path())
        else:
            messages[id] = disscussion.get_path()
        print(f"Reaction : {reaction}")
        print(f"User : {user}")

        disscussion.next_message(opt)

        if disscussion.isLastMessage() == False:
            botAnswer = await send(reaction.message, disscussion)
            match disscussion.show_message():
                case Messages.FIRST_MESSAGE:
                    await botAnswer.add_reaction("⌨️")
                    await botAnswer.add_reaction("🇫")
                case Messages.R | Messages.RL | Messages.RR:
                    await botAnswer.add_reaction('✅')
                    await botAnswer.add_reaction('❌')
                case Messages.RRR | Messages.RLR:
                    await botAnswer.add_reaction('🐉')
                    await botAnswer.add_reaction('<:greatsword:1191087208581574726>')
            conversation.set("utilisateurs", utilisateurs)
            conversation.set("message", messages)
            saveConversations(dataConv, conversation, open(
                "historique/conversations.json", "r+"))

        else:
            print(f"MESSAGE : {disscussion.show_message()}")
            botAnswer = await send(reaction.message, disscussion)
            disscussion.goRoot()
            messages[id] = []
            conversation.set("message", messages)
            saveConversations(dataConv, conversation, open(
                "historique/conversations.json", "r+"))

            discussion_on = False


# ANCHOR - fonction principales

################################ FONCTION PRINCIPALES ################################

# Lance la création d'un nouveau set

# ANCHOR - !new_set
@bot.command(name="new_set")
async def new_set(ctx, armorName=None, weaponName=None):
    global sets, data
    if armorName == None or weaponName == None:
        await ctx.channel.send("Saisissez le nom de l'armure et de l'arme")
        return
    armorId = 0
    weaponId = 0
    for i in range(len(ARMORS)):
        if armorName.lower() in ARMORS[i].name.lower():
            armorId = ARMORS[i].id
    for i in range(len(WEAPONS)):
        if weaponName.lower() in WEAPONS[i].name.lower():
            weaponId = WEAPONS[i].id
    if armorId == 0 and weaponId == 0:
        await ctx.channel.send("Armure et arme introuvable (probablement inexsitante ou mal orthographié)")
        return
    elif armorId == 0:
        await ctx.channel.send("Armure introuvable (probablement inexsitante ou mal orthographié)")
        return
    elif weaponId == 0:
        await ctx.channel.send("Arme introuvable (probablement inexsitante ou mal orthographié)")
        return
    else:
        sets.append(newSet(ARMORS, armorId, WEAPONS, weaponId))
        saveSets(data, sets, file=open(path, "r+"))
        await ctx.channel.send("set registered !")
        return

# Génère un set à partir du monstre chassé et de l'arme utilisé par l'utilisateur

# ANCHOR - !make_set


@bot.command(name="make_set")
async def make_set(ctx):
    monster = None
    monsterWeakness = None
    monsterElement = None
    armor = None
    weapon = None

    monsterView = MonsterView()
    await ctx.send("sélectionnez une cible", view=monsterView)
    await monsterView.wait()

    for m in MONSTERS:
        if m.name == monsterView.value:
            monster = m
            break

    for weakness in monster.weaknesses:
        if weakness["stars"] == 3:
            monsterWeakness = weakness["element"]
            break

    if monster.elements == []:
        monsterElement = "dragon"
    else:
        monsterElement = monster.elements[0]

    for a in ARMORS:
        if a.pieces[0]["resistances"][monsterElement] == 3:
            armor = a
            break

    await ctx.send(armor.name+" "+str(armor.id))

    weaponView = WeaponView()
    await ctx.send("Sélectionnez une arme", view=weaponView)
    await weaponView.wait()

    for w in WEAPONS:
        if w.type == weaponView.value:
            if w.elements != []:
                for e in w.elements:
                    if e["type"] == monsterWeakness:
                        weapon = w
                        break

            elif w.ammo != None:
                for a in w.ammo:
                    if a["type"] == monsterWeakness or a["type"] == "flaming" and monsterWeakness == "fire":
                        weapon = w
                        break

    await ctx.send(f'Pour cette chasse, je recommande l\'armure "{armor.name}". En ce qui concerne l\'arme, le meilleur choix serait "{weapon.name}" pour ses dégats élémentaires et votre style de jeu.')
    sets.append(newSet(ARMORS, armor.id, WEAPONS, weapon.id))
    saveSets(data, sets, file=open(path, "r+"))
    await ctx.channel.send("le set a été enregistré.")

# Montre à l'utilisateur tout ses sets

# ANCHOR - !get_sets


@bot.command(name="get_sets")
async def get_sets(ctx):
    global sets
    historique.append("!get_sets")
    saveHistory(data, historique, file=open(path, "r+"))
    nb = 1
    for s in sets:
        nextSet = NextButton()
        await ctx.send(f"SET {nb}")
        embedArmor = discord.Embed()
        embedArmor.add_field(name="ARMOR", value=s.armor.name, inline=False)
        await ctx.send(embed=embedArmor)

        for i in range(len(s.armor.pieces)):
            embedPiece = discord.Embed()
            embedPiece.add_field(
                name=s.armor.pieces[i]["type"], value=s.armor.pieces[i]["name"], inline=False)
            try:
                embedPiece.set_image(
                    url=s.armor.pieces[i]["assets"]["imageMale"])
            except:
                print('NO ASSETS')
            await ctx.send(embed=embedPiece)

        embedWeapon = discord.Embed()
        embedWeapon.add_field(
            name="WEAPON", value=s.weapon.name+elementEmoji(s.weapon), inline=False)
        embedWeapon.set_image(url=s.weapon.assets["icon"])
        nb += 1
        if nb <= len(sets):
            await ctx.send(embed=embedWeapon, view=nextSet)
            await nextSet.wait()
        else:
            await ctx.send(embed=embedWeapon)

# Montre à l'utilisateur le SET de son choix

# ANCHOR - !get_set


@bot.command(name="get_set")
async def get_set(ctx, number=None):
    global sets
    if number == None or number.isnumeric() == False:
        await ctx.send(f"Entrez un numéro de set")
        return

    number = int(number)-1
    historique.append(f"!get_set {number+1}")
    saveHistory(data, historique, file=open(path, "r+"))
    if number > len(sets)-1:
        await ctx.send("Vous n'avez pas tant de sets")
        return
    elif number < 0:
        await ctx.send(f"Le set numéro {number+1} ne correspond à rien")
        return

    await ctx.send(f"SET {number+1}")
    embedArmor = discord.Embed()
    embedArmor.add_field(
        name="ARMOR", value=sets[number].armor.name, inline=False)
    await ctx.send(embed=embedArmor)

    for i in range(len(sets[number].armor.pieces)):
        nextPiece = NextButton()

        embedPiece = discord.Embed()
        embedPiece.add_field(
            name=sets[number].armor.pieces[i]["type"], value=sets[number].armor.pieces[i]["name"], inline=False)
        try:
            embedPiece.set_image(
                url=sets[number].armor.pieces[i]["assets"]["imageMale"])
        except:
            print('NO ASSETS')
        await ctx.send(embed=embedPiece, view=nextPiece)
        await nextPiece.wait()

    embedWeapon = discord.Embed()
    embedWeapon.add_field(name="WEAPON", value=sets[number].weapon.name +
                          elementEmoji(sets[number].weapon), inline=False)
    embedWeapon.set_image(url=sets[number].weapon.assets["icon"])
    await ctx.send(embed=embedWeapon)


@bot.command(name="delete_set")
async def delete_set(ctx, number=None):
    global sets
    if number == None or number.isnumeric() == False:
        await ctx.send(f"Entrez le numéro du set à supprimer")
        return

    number = int(number)-1
    historique.append(f"!delete_set {number+1}")
    saveHistory(data, historique, file=open(path, "r+"))
    if number > len(sets)-1:
        await ctx.send("Vous n'avez pas tant de sets")
        return
    elif number < 0:
        await ctx.send(f"Le set numéro {number+1} ne correspond à rien")
        return

    sets.pop(number)
    saveSets(data, sets, file=open(path, "r+"))
    await ctx.channel.send("le set a été supprimé.")


@bot.command(name="stat_set")
async def stat_set(ctx, number=None):
    global sets
    attack = 0
    element = None
    defense = 0
    resistances = {
        "fire": 0,
        "water": 0,
        "ice": 0,
        "thunder": 0,
        "dragon": 0
    }

    if number == None or number.isnumeric() == False:
        await ctx.send(f"Entrez le numéro du set dont vous souhaiter voir les statistique")
        return

    number = int(number)-1
    historique.append(f"!stat_set {number+1}")
    saveHistory(data, historique, file=open(path, "r+"))
    if number > len(sets)-1:
        await ctx.send("Vous n'avez pas tant de sets")
        return
    elif number < 0:
        await ctx.send(f"Le set numéro {number+1} ne correspond à rien")
        return

    attack = sets[number].weapon.attack["raw"]
    if sets[number].weapon.elements:
        element = sets[number].weapon.elements[0]["type"]
    defense = sets[number].armor.pieces[0]["defense"]["max"] * \
        len(sets[number].armor.pieces)
    resistances = {"fire": sets[number].armor.pieces[0]["resistances"]["fire"] * 5,
                   "water": sets[number].armor.pieces[0]["resistances"]["water"]*5,
                   "ice": sets[number].armor.pieces[0]["resistances"]["ice"]*5,
                   "thunder": sets[number].armor.pieces[0]["resistances"]["thunder"]*5,
                   "dragon": sets[number].armor.pieces[0]["resistances"]["dragon"]*5}
    embed=discord.Embed(title="Stats",description=f"Voici les statistique du set numéro {number+1}")
    embed.add_field(name="Attack",value=attack)
    if elementEmoji(sets[number].weapon)!="":
        embed.add_field(name="Element",value=elementEmoji(sets[number].weapon))
    else:
        embed.add_field(name="Element",value="neutre")
    embed.add_field(name="Defense",value=defense)
    embed.add_field(name="Fire resistance <:Fire:1192522472151584909>",value=resistances["fire"])
    embed.add_field(name="Water resistance <:water:1192522477008588871>",value=resistances["water"])
    embed.add_field(name="Ice resistance <:ice:1192522473418264667>",value=resistances["ice"])
    embed.add_field(name="Thunder resistance <:thunder:1192522474877878423>",value=resistances["thunder"])
    embed.add_field(name="Dragon resistance <:Dragon:1192522469521756265>",value=resistances["dragon"])
    
    await ctx.send(embed=embed)
    
# ANCHOR - Bot

################################ BOT ################################

# Suppression des messages (10 messages)


@bot.command(name="delete")
async def delete(ctx):
    historique.append("!delete")
    saveHistory(data, historique, file=open(path, "r+"))
    ms = ctx.channel.history(limit=10)

    async for message in ms:
        await message.delete()
        print("deleted")


@bot.event
async def on_ready():
    print("Le bot est prêt !")


# Accueil nouveau membre

# ANCHOR - on_member_join
@bot.event
async def on_member_join(member):
    general_channel = bot.get_channel(1167470031345553502)
    await general_channel.send("Bienvenue sur le serveur ! " + member.name)

# ANCHOR - on_message


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

                await send(message, Disscussion)

    await bot.process_commands(message)

bot.run(os.getenv("BOT_ID"))
