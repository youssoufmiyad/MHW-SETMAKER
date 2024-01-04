import os
import json
from models.armorModel import *
from models.weaponsModel import *


class Set:
    def __init__(self, armor, weapon):
        self.armor = armor
        self.weapon = weapon

# Chargement de la sauvegarde


def setsLoading(data):
    sets = []

    for d in data["sets"]:
        sets.append(
            Set(
                Armor(d["armor"]["id"], d["armor"]["name"], d["armor"]["rank"], d["armor"]["pieces"], d["armor"]["bonus"]),
                Weapon(d["weapon"]["id"], d["weapon"]["name"], d["weapon"]["type"], d["weapon"]["rarity"], d["weapon"]["attack"], d["weapon"]["elements"], d["weapon"]["crafting"], d["weapon"]["assets"], d["weapon"]["damageType"], d["weapon"]["attributes"])
            )
        )

    return sets
