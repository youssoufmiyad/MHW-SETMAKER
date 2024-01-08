import os
import json

from data_structures.hashMap import avancement_conversation

############### GESTION DE L'HASHMAP CONTENANT L'ETAT DES CONVERSATIONS ###############

# Vérification de l'existence d'une sauvegarde


def saveConversationExist():
    if os.path.isfile("historique/conversations.json"):
        print("file exist")
        file = open("historique/conversations.json", "r+")
        data = json.load(file)
    else:
        print("file doesnt exist")
        file = open("historique/conversations.json", "w")
        file.write('{"conversations":[]}')
        data = json.loads('{"conversations":[]}')
    return data

# Chargement de la hashmap


def conversationsLoading(data):
    conversation = avancement_conversation
    conversation.set("conversations", data)
    return conversation

# Sauvegarde des changement


def saveConversations(data, conversation, file):
    data['conversations'] = conversation.get("conversations")

    file.seek(0)
    json.dump(data, file, indent=4)
    file.truncate()
