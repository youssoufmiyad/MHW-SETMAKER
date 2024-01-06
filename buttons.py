import discord
from datetime import datetime
class NextButton(discord.ui.View):
    def __init__(self):
        super().__init__()
    
    @discord.ui.button(label="next", style=discord.ButtonStyle.gray)
    async def function_name(self, interaction: discord.Interaction,button: discord.ui.Button):
        button.disabled = True
        button.view.stop()
        await interaction.response.edit_message( view=self)
        
    