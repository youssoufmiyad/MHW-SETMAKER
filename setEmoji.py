import discord
from assets.emoji import *

def setWeaponOptions():
    arr=[]
    arr.append(discord.SelectOption(label="great-sword",emoji=GREATSWORD))
    arr.append(discord.SelectOption(label="lance",emoji=LANCE))
    arr.append(discord.SelectOption(label="heavy-bowgun",emoji=HEAVY_BOWGUN))
    arr.append(discord.SelectOption(label="hunting-horn",emoji=HUNTING_HORN))
    arr.append(discord.SelectOption(label="sword-and-shield",emoji=SWORD_AND_SHIELD))
    arr.append(discord.SelectOption(label="dual-blades",emoji=DUAL_BLADES))
    arr.append(discord.SelectOption(label="bow",emoji=BOW))
    arr.append(discord.SelectOption(label="light-bowgun",emoji=LIGHT_BOWGUN))
    arr.append(discord.SelectOption(label="long-sword",emoji=LONGSWORD))
    arr.append(discord.SelectOption(label="hammer",emoji=HAMMER))
    arr.append(discord.SelectOption(label="gunlance",emoji=GUNLANCE))
    arr.append(discord.SelectOption(label="charge-blade",emoji=CHARGE_BLADE))
    arr.append(discord.SelectOption(label="switch-axe",emoji=SWITCH_AXE))
    arr.append(discord.SelectOption(label="insect-glaive",emoji=INSECT_GLAIVE))
    return arr