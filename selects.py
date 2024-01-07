from typing import Any, Optional
import discord
from API import *
from assets.emoji import *
from discord.interactions import Interaction
from setEmoji import *
monstersName=[]
MONSTERS
nb=0
for m in MONSTERS:
    if nb == 24:
        break
    else:
        monstersName.append(discord.SelectOption(label=m.name))
        nb+=1
    
class MonsterView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value=None
        
    @discord.ui.select(placeholder="Select a monster",options=monstersName,min_values=1,max_values=1)
    async def callback(self, interaction: discord.Interaction,select: discord.ui.Select):
        select.placeholder=select.values[0]
        select.disabled=True
        select.view.stop()
        self.value=select.values[0]
        await interaction.response.edit_message(content=f"you choose {select.values[0]}",view=self)

weaponsName=setWeaponOptions()
weaponEmoji=""
    
class WeaponView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value=None
        
    @discord.ui.select(placeholder="Select a weapon",options=weaponsName,min_values=1,max_values=1)
    async def callback(self, interaction: discord.Interaction,select: discord.ui.Select):
        select.placeholder=select.values[0]
        select.disabled=True
        select.view.stop()
        self.value=select.values[0]
        await interaction.response.edit_message(content=f"you choose {select.values[0]}",view=self)