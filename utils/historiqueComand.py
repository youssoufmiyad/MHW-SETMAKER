import os
import json

from data_structures.liste import chained_list

###################### GESTION DE LA LIST CONTENANT L'HISTORIQUE ######################

# Vérification de l'existence d'une sauvegarde

def saveHistoryExist(path):
    if os.path.isfile(path):
        file = open(path, "r+")
        data = json.load(file)
    else:
        file = open(path, "w")
        file.write('{"commandes":[],"sets":[]}')
        data = json.loads('{"commandes":[],"sets":[]}')
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