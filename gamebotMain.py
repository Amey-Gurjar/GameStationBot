import discord
from discord.ui import Button, View
from discord.ext import commands
from json import load
selfDelete = 12.0
playersList = {}
finalWinPos = {}
def dataJson():
    mainJsonFile = load(open("mainData.json", "r"))
    return mainJsonFile
class gameBot(commands.Cog, name="gameBot"):
    gameWinPos = dataJson()["gameData"]["gameWinPos"]
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(name="game")
    async def game(self, ctx, player: discord.Option(discord.Member, description="Player To Play With")):
        await ctx.defer()
        if player.bot != True and ctx.author.id != player.id:
            if len(playersList) == 0:
                playersList[ctx.author.id] = 0
                playersList[player.id] = 0
                embedSelect = discord.Embed(title="Select Your Player", description=f"**<@{ctx.author.id}> V/S <@{player.id}>\nX or O**", color=discord.Colour.from_rgb(255, 255, 0))
                viewSelectBtn = View()
                for i in range(len(dataJson()["gameData"]["playersObject"])):
                    viewSelectBtn.add_item(Button(label=dataJson()["gameData"]["playersObject"][i], custom_id=dataJson()["gameData"]["playersObject"][i]))
                await ctx.send_followup(embed=embedSelect, view=viewSelectBtn)
            else:
                await ctx.send_followup(f"Somebody Is Already Playing!", delete_after=selfDelete)
        else:
            await ctx.send_followup(f"That Is A Bot!", delete_after=selfDelete)
    @commands.Cog.listener()
    async def on_interaction(self, interaction):
        if interaction.user.bot != True:
            if interaction.type == discord.InteractionType.component:
                if interaction.user.id in list(playersList.keys()):
                    if interaction.data["custom_id"] in dataJson()["gameData"]["playersObject"]:
                        playersList[interaction.user.id] = interaction.data["custom_id"]
                        playersList[[x for x in playersList if x!=interaction.user.id][0]] = [z for z in dataJson()["gameData"]["playersObject"] if z!=playersList[interaction.user.id]][0]
                        gameEmbed = discord.Embed(title="Tic Tac Toe", description=f"**<@{list(playersList.keys())[0]}> V/S <@{list(playersList.keys())[1]}>**", color= discord.Colour.from_rgb(255, 255, 0))
                        playerPos = {}
                        async def checkWinPos(interaction, btnIndex):
                            async def checkFinal():
                                print(finalWinPos[interaction.user.id])
                                if len(finalWinPos[interaction.user.id]) == 3:
                                    await interaction.response.send_message(f"<@{interaction.user.id}> Has Won!!", delete_after=selfDelete)
                                    await interaction.message.delete()
                                    playersList.clear()
                                    playerPos.clear()
                                    finalWinPos.clear()
                                    return None
                            if interaction.user.id in list(playerPos.keys()):
                                playerPos[interaction.user.id].append(btnIndex)
                            else:
                                playerPos[interaction.user.id] = []
                                playerPos[interaction.user.id].append(btnIndex)
                            if len(playerPos[interaction.user.id]) == 3:
                                for winPos in gameBot.gameWinPos:
                                    for btnIndex in playerPos[interaction.user.id]:
                                        if btnIndex in winPos:
                                            if interaction.user.id not in list(finalWinPos.keys()):
                                                    finalWinPos[interaction.user.id] = []
                                                    finalWinPos[interaction.user.id].append(btnIndex)
                                                    await checkFinal()
                                                    break
                                            else:
                                                if len(finalWinPos[interaction.user.id]) < 3:
                                                    finalWinPos[interaction.user.id].append(btnIndex)
                                                    await checkFinal()
                                                    break
                        class gameBtnView(View):
                            @discord.ui.button(label="‎", custom_id="gameBtn0", row=0)
                            async def gameBtn0(self, button, interaction):
                                await checkWinPos(interaction, 0)
                                try:
                                    button.label = playersList[interaction.user.id]
                                    button.disabled = True
                                    await interaction.response.edit_message(view=self)
                                except Exception as e:
                                    print(e)
                            @discord.ui.button(label="‎", custom_id="gameBtn1", row=0)
                            async def gameBtn1(self, button, interaction):
                                await checkWinPos(interaction, 1)
                                try:
                                    button.label = playersList[interaction.user.id]
                                    button.disabled = True
                                    await interaction.response.edit_message(view=self)
                                except Exception as e:
                                    print(e)
                            @discord.ui.button(label="‎", custom_id="gameBtn2", row=0)
                            async def gameBtn2(self, button, interaction):
                                await checkWinPos(interaction, 2)
                                try:
                                    button.label = playersList[interaction.user.id]
                                    button.disabled = True
                                    await interaction.response.edit_message(view=self)
                                except Exception as e:
                                    print(e)
                            @discord.ui.button(label="‎", custom_id="gameBtn3", row=1)
                            async def gameBtn3(self, button, interaction):
                                await checkWinPos(interaction, 3)
                                try:
                                    button.label = playersList[interaction.user.id]
                                    button.disabled = True
                                    await interaction.response.edit_message(view=self)
                                except Exception as e:
                                    print(e)
                            @discord.ui.button(label="‎", custom_id="gameBtn4", row=1)
                            async def gameBtn4(self, button, interaction):
                                await checkWinPos(interaction, 4)
                                try:
                                    button.label = playersList[interaction.user.id]
                                    button.disabled = True
                                    await interaction.response.edit_message(view=self)
                                except Exception as e:
                                    print(e)
                            @discord.ui.button(label="‎", custom_id="gameBtn5", row=1)
                            async def gameBtn5(self, button, interaction):
                                await checkWinPos(interaction, 5)
                                try:
                                    button.label = playersList[interaction.user.id]
                                    button.disabled = True
                                    await interaction.response.edit_message(view=self)
                                except Exception as e:
                                    print(e)
                            @discord.ui.button(label="‎", custom_id="gameBtn6", row=2)
                            async def gameBtn6(self, button, interaction):
                                await checkWinPos(interaction, 6)
                                try:
                                    button.label = playersList[interaction.user.id]
                                    button.disabled = True
                                    await interaction.response.edit_message(view=self)
                                except Exception as e:
                                    print(e)
                            @discord.ui.button(label="‎", custom_id="gameBtn7", row=2)
                            async def gameBtn7(self, button, interaction):
                                await checkWinPos(interaction, 7)
                                try:
                                    button.label = playersList[interaction.user.id]
                                    button.disabled = True
                                    await interaction.response.edit_message(view=self)
                                except Exception as e:
                                    print(e)
                            @discord.ui.button(label="‎", custom_id="gameBtn8", row=2)
                            async def gameBtn8(self, button, interaction):
                                await checkWinPos(interaction, 8)
                                try:
                                    button.label = playersList[interaction.user.id]
                                    button.disabled = True
                                    await interaction.response.edit_message(view=self)
                                except Exception as e:
                                    print(e)
                        await interaction.followup.send(embed=gameEmbed, view=gameBtnView())
                        await interaction.message.delete()
def setup(bot):
    bot.add_cog(gameBot(bot))