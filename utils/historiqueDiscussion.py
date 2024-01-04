import os
import json

from data_structures.hashMap import avancement_conversation

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