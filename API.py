import urllib3
import json
from types import SimpleNamespace
from models import armorModel, monstersModel,weaponsModel


def getMonsters():
    resp = urllib3.request("GET", "https://mhw-db.com/monsters").json()
    m = monstersModel.Monsters()
    nb = 0
    while True:
        try:
            m.all.append(monstersModel.Monster(**resp[nb]))
            nb += 1
        except:
            print("done")
            break
    return m


def getLargeMonsters():
    resp = urllib3.request("GET", 'https://mhw-db.com/monsters?q={"type":"Large"}').json()
    largeMonsters = monstersModel.Monsters()
    nb = 0
    while True:
        try:
            largeMonsters.all.append(monstersModel.Monster(**resp[nb]))
            nb+=1
        except:
            print("done")
            break
    return largeMonsters.all


def getArmors():
    resp = urllib3.request("GET", "https://mhw-db.com/armor/sets",timeout=10).json()
    s = armorModel.Armors()
    nb = 0
    while True:
        try:
            s.all.append(armorModel.Armor(**resp[nb]))
            nb += 1
        except:
            print("done")
            break
    return s.all


def getWeapons():
    resp = urllib3.request(
        "GET", 'https://mhw-db.com/weapons?p={"id":true,"name":true,"type":true,"rarity":true,"attack":true,"elements":true,"crafting":true,"assets":true,"damageType":true,"attributes":true}', timeout=10).json()
    w = weaponsModel.Weapons()
    nb = 0
    while True:
        try:
            w.all.append(weaponsModel.Weapon(**resp[nb]))
            nb += 1
        except:
            print("done")
            break

    return w.all

