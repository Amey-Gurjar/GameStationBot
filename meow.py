from discord.ext import commands
from discord.ui import Button, View
import discord
selfDelete = 10.0
playersList = []
class gameBot(commands.Cog, name="gameBot"):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(name="game")
    async def game(self, ctx, player: discord.Option(discord.Member, description="Player To Play With")):
        await ctx.defer()
        if player.bot != True:
            playersList.append(ctx.author)
            playersList.append(player)
            embedSelect = discord.Embed(title="Select Your Player", description="X or O")
            selectView = View()
            for i in range(len(data))
            selectView.add_item(Button(label="X", custom_id="X"))
            selectView.add_item(Button(label="O", custom_id="O"))
            await ctx.send_followup(embed=embedSelect, view=selectView)
            print(playersList)
        else:
            await ctx.send_followup(f"That Is A Bot!", delete_after=selfDelete)
def setup(bot):
    bot.add_cog(gameBot(bot))