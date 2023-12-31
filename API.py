import urllib3
import json
from types import SimpleNamespace
from models import monstersModel,weaponsModel,setModel


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
    resp = urllib3.request("GET", "https://mhw-db.com/monsters").json()
    monsters = getMonsters()
    largeMonsters = monstersModel.Monsters()
    nb = 0
    for monster in monsters.all:
        if monster.type == "large":
            largeMonsters.all.append(monster)
    return monsters


def getSets():
    resp = urllib3.request("GET", "https://mhw-db.com/armor/sets",timeout=10).json()
    s = setModel.Sets()
    nb = 0
    while True:
        try:
            s.all.append(setModel.Set(**resp[nb]))
            nb += 1
        except:
            print("done")
            break
    return s


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

    return w


m = getSets()
for i in m.all:
    print(i.toString(), "\n")
