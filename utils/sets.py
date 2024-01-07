import os
import json
import urllib3

from models.armorModel import *
from models.weaponsModel import *
from utils.historiqueComand import *
from API import *


class Set:
    def __init__(self, armor, weapon):
        self.armor = armor
        self.weapon = weapon

    def toString(self):
        return (f"ARMOR\n{self.armor.name}\nWEAPON\n{self.weapon.name}")


# Chargement de la sauvegarde


def setsLoading(data):
    sets = []

    for d in data["sets"]:
        sets.append(
            Set(
                Armor(d["armor"]["id"], d["armor"]["name"], d["armor"]
                      ["rank"], d["armor"]["pieces"], d["armor"]["bonus"]),
                Weapon(d["weapon"]["id"], d["weapon"]["name"], d["weapon"]["type"], d["weapon"]["rarity"], d["weapon"]["attack"], d["weapon"]
                       ["elements"], d["weapon"]["crafting"], d["weapon"]["assets"], d["weapon"]["damageType"], d["weapon"]["attributes"])
            )
        )
    return sets

# Création de set


def newSet(armors, armorID, weapons, weaponID):
    global newWeapon, newArmor
    nb = 0
    for w in weapons:
        # print(f"WEAPON : {w.name}")
        if w.id == weaponID:
            newWeapon = w
            break

    for a in armors:
        if a.id == armorID:
            newArmor = a
            break
    return(
        Set(
            Armor(newArmor.id, newArmor.name, newArmor.rank,
                  newArmor.pieces, newArmor.bonus),
            Weapon(newWeapon.id, newWeapon.name, newWeapon.type, newWeapon.rarity, newWeapon.attack,
                   newWeapon.elements, newWeapon.crafting, newWeapon.assets, newWeapon.damageType, newWeapon.attributes)
        ))


# Sauvegarde des sets


def saveSets(data, sets, file):
    setJSON = f""
    print(f"STR : {sets[0].armor.toJSON()}")
    data['sets'] = []
    for s in range(len(sets)):
        data['sets'].append({"armor": sets[s].armor.toJSON(),"weapon":sets[s].weapon.toJSON()})
    file.seek(0)
    json.dump(data, file, indent=4)
    file.truncate()
