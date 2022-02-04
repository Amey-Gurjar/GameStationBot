from discord.ext.commands import Bot
import discord
from json import load
mainIntents = discord.Intents.default()
mainIntents.members = True
mainIntents.presences = True
mainBot = Bot(debug_guilds=load(open("token.json"))["guild"], activity=discord.Activity(type=discord.ActivityType.listening, name=f"GameStation"), intents=mainIntents, status=discord.Status.dnd)
mainBotExtention = ["valoBot", "ptsBot", "mainMeme", "weatherBot"]
if __name__ == "__main__":
    for i in mainBotExtention:
        mainBot.load_extension(i)
mainBot.run(load(open("token.json", "r"))["token"])