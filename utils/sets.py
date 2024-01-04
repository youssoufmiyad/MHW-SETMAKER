import os
import json
from models.armorModel import *


# Chargement de la sauvegarde

def setsLoading(data):
    sets = []
    
    for d in data["sets"]:
        sets.append(Armor(d["armor"]["id"],d["armor"]["name"],d["armor"]["rank"],d["armor"]["pieces"],d["armor"]["bonus"]))

    return sets
