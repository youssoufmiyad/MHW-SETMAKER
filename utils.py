import os
import json

from data_structures.liste import chained_list
from data_structures.hashMap import avancement_conversation

###################### GESTION DE LA LIST CONTENANT L'HISTORIQUE ######################

# Vérification de l'existence d'une sauvegarde


def saveHistoryExist(path):
    if os.path.isfile(path):
        file = open(path, "r+")
        data = json.load(file)
    else:
        file = open(path, "w")
        file.write('{"commandes":[]}')
        data = json.loads('{"commandes":[]}')
    return data

# Chargement de la sauvegarde


def historyLoading(data):
    cl = chained_list()
    for d in data["commandes"]:
        cl.append(d)
    return cl

# Sauvegarde des changement


def saveHistory(data, historique, file):
    historiqueJSON = '['
    h = ""
    for i in range(historique.lenght()):
        if i < historique.lenght()-1:
            h += '"'+str(historique.get(i))+'", '
        else:
            h += '"'+str(historique.get(i))+'"'
    historiqueJSON += h+']'
    data['commandes'] = json.loads(historiqueJSON)
    file.seek(0)
    json.dump(data, file, indent=4)
    file.truncate()

############### GESTION DE L'HASHMAP CONTENANT L'ETAT DES CONVERSATIONS ###############

# Vérification de l'existence d'une sauvegarde


def saveConversationExist():
    if os.path.isfile("historique/conversations.json"):
        file = open("historique/conversations.json", "r+")
        data = json.load(file)
    else:
        file = open("historique/conversations.json", "w")
        file.write('{"utilisateurs":[],"message":[]}')
        data = json.loads('{"utilisateurs":[],"message":[]}')
    return data

# Chargement de la hashmap


def conversationsLoading(data):
    conversation = avancement_conversation
    conversation.set("utilisateurs", data["utilisateurs"])
    conversation.set("message", data["message"])
    return conversation

# Sauvegarde des changement


def saveConversations(data, conversation, file):
    data['utilisateurs'] = conversation.get("utilisateurs")
    data['message'] = conversation.get("message")

    file.seek(0)
    json.dump(data, file, indent=4)
    file.truncate()


# conv = conversationsLoading(saveConversationExist())
# conv.set("utilisateurs", ["HAHA"])
# saveConversations(saveConversationExist(), conv, file=open(
#     "historique/conversations.json", "r+"))


def rightOrLeft(message):
    if message == "oui" or message in "fonctionnement" or message in "monstres" or message in "1":
        return "right"
    elif message == "non" or message in "commandes" or message in "armes" or message in "2":
        return "left"


def rightOrLeftReaction(reaction):
    print("REACT = ", str(reaction))
    if str(reaction) == "✅":
        return "right"
    elif str(reaction) == "❌":
        return "left"
    else:
        return "not read"


async def send(ctx, disscussion, reactions):
    if disscussion.isLastMessage()==False:
        botAnswer = await ctx.channel.send(disscussion.show_message())
        for r in reactions:
            await botAnswer.add_reaction(r)
        return botAnswer
