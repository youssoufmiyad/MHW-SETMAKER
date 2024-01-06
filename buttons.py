from typing import Any, Optional
import discord
from API import *
from discord.interactions import Interaction
class NextButton(discord.ui.View):
    def __init__(self):
        super().__init__()
    
    @discord.ui.button(label="next", style=discord.ButtonStyle.gray)
    async def next(self, interaction: discord.Interaction,button: discord.ui.Button):
        button.disabled = True
        button.view.stop()
        await interaction.response.edit_message( view=self)
        

option=[]
monsters = getLargeMonsters()
nb=0
for m in monsters:
    if nb == 24:
        break
    else:
        option.append(discord.SelectOption(label=m.name))
        nb+=1
    
class MonsterView(discord.ui.View):
    def __init__(self):
        super().__init__()
        
    @discord.ui.select(placeholder="Select a monster",options=option,min_values=1,max_values=1)
    async def callback(self, interaction: discord.Interaction,select: discord.ui.Select):
        select.placeholder=select.values[0]
        select.disabled=True
        select.view.stop()
        await interaction.response.edit_message(content=f"you choose {select.values[0]}",view=self)
