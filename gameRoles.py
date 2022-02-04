from discord import Bot
import discord
from json import load
from discord.ui import Button, View
mainIntents = discord.Intents.default()
mainIntents.members = True
mainIntents.presences = True
mainBot = Bot(debug_guilds=load(open("token.json"))["guild"], activity=discord.Activity(type=discord.ActivityType.watching, name=f"GameStation"), intents=mainIntents, status=discord.Status.dnd)
mainData = load(open("mainData.json", "r"))["gameRoles"]
@mainBot.event 
async def on_message(ctx):
    if ctx.author != mainBot.user:
        mainEmbed = discord.Embed(title="GAME ROLES", description="**Welcome to the GameStation!**.\nTake Game Roles According To The Games You Play", color= discord.Colour.from_rgb(255, 255, 0))
        mainEmbed.set_image(url="https://images.pexels.com/photos/275033/pexels-photo-275033.jpeg?cs=srgb&dl=pexels-pixabay-275033.jpg&fm=jpg")
        mainView = View()
        for i in range(len(mainData)):
            gameButton = Button(label=list(mainData.keys())[i], custom_id=list(mainData.keys())[i], style=discord.ButtonStyle.green)
            mainView.add_item(gameButton)
        await ctx.channel.send(embed=mainEmbed, view=mainView)
mainBot.run(load(open("token.json", "r"))["token"])