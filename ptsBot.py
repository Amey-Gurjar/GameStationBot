import discord
from discord.ext import commands
from json import load
from discord.ui import Button, View
from threading import Thread
import firebase_admin
from firebase_admin import firestore, credentials
ameydbCollection = "gameStationPts"
ameydbCollectionLvl = "gameStationLvl"
ameydbCollectionLvlCheck = "gameStationLvlCheck"
ameydbCollectionLvlComplete = "gameStationLvlComplete"
mainDataList = []
stringReplace = "!#$^&*()<@>"
selfDelete = 12.0
firebase_admin.initialize_app(credentials.Certificate(load(open("mainDb.json", "r"))))
ameydb = firestore.client()
class dataLoad(Thread):
    def jsonDataLoader():
        mainData = load(open("mainData.json", "r"))
        return mainData
class errorHandler(commands.Cog, name="errorHandler"):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        print(error)     
class levelingSystem(commands.Cog, name="levelingSystem"):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author.bot == False:
            try:
                userMessageNum = int(ameydb.collection(ameydbCollectionLvl).document(str(ctx.author.id)).get().to_dict()[ameydbCollectionLvl])
            except:
                userMessageNum = 0
            try:
                userCurrentLvl = int(ameydb.collection(ameydbCollectionLvlComplete).document(str(ctx.author.id)).get().to_dict()[ameydbCollectionLvlComplete])
            except:
                userCurrentLvl = 0
                ameydb.collection(ameydbCollectionLvlComplete).document(str(ctx.author.id)).set({ameydbCollectionLvlComplete: f"{userCurrentLvl}"})
            try:
                userLvlCheck = int(ameydb.collection(ameydbCollectionLvlCheck).document(str(ctx.author.id)).get().to_dict()[ameydbCollectionLvlCheck])
            except: 
                userLvlCheck = 1
            ameydb.collection(ameydbCollectionLvl).document(str(ctx.author.id)).set({ameydbCollectionLvl: f"{int(userMessageNum) + int(1)}"})
            if userMessageNum == userLvlCheck:
                try:
                    ameydb.collection(ameydbCollectionLvlCheck).document(str(ctx.author.id)).set({ameydbCollectionLvlCheck: f"{int(userMessageNum) * int(2)}"})
                    userCurrentLvl = ameydb.collection(ameydbCollectionLvlComplete).document(str(ctx.author.id)).set({ameydbCollectionLvlComplete: f"{int(userCurrentLvl) + int(1)}"})
                    updatedUserLvl = int(ameydb.collection(ameydbCollectionLvlComplete).document(str(ctx.author.id)).get().to_dict()[ameydbCollectionLvlComplete])
                    try:
                        currentPoints = int(ameydb.collection(ameydbCollection).document(str(ctx.author.id)).get().to_dict()[ameydbCollection])
                    except Exception as e:
                        currentPoints = 0
                    ameydb.collection(ameydbCollection).document(str(ctx.author.id)).set({ameydbCollection: f"{int(currentPoints) + int(50)}"})
                    await ctx.author.send(f"50 GameStation Points Has Been Added To Your GameStation Account As A Level Up Reward.")
                    lvlCheckChannel = await self.bot.fetch_channel(dataLoad.jsonDataLoader()["gsPoints"]["gsLvlChannel"])
                    await lvlCheckChannel.send(f"<@{ctx.author.id}> You Just Leveled Up To {updatedUserLvl} Lvl.")
                except Exception as e:
                    print(e)
class addPoints(commands.Cog, name="addPoints"):
    def __init__(self, bot): 
        self.bot = bot
    @commands.slash_command(name="pointsadd", description="To Add Points To Any Member.")
    async def pointsadd(self, ctx, user: discord.Option(discord.Member, description="Member To Add Points"), points: discord.Option(int, description="Number Of Points To Add.")):
        await ctx.defer()
        if ctx.author != self.bot.user and ctx.author.guild_permissions.administrator == True:
            if ctx.channel.id == dataLoad.jsonDataLoader()["gsPoints"]["managePtsChannel"]:
                try:
                    currentPoints = ameydb.collection(ameydbCollection).document(str(user.id)).get().to_dict()[ameydbCollection]
                except:
                    currentPoints = 0
                ameydb.collection(ameydbCollection).document(str(user.id)).set({ameydbCollection: f"{int(currentPoints) + int(points)}"})
                memberObject = await ctx.guild.fetch_member(user.id)
                await ctx.respond(f"{points} GameStation Points Added To <@{user.id}>")
                await memberObject.send(f"{points} GameStation Points Has Been Added To Your GameStation Account.")
            else:
                await ctx.respond(f"<@{ctx.author.id}> This Command Will Only Work In <#{dataLoad.jsonDataLoader()['gsPoints']['managePtsChannel']}>", delete_after=selfDelete)
        else: 
            await ctx.respond(f"<@{ctx.author.id}> You Don't The Permissions To Use This Command.", delete_after=selfDelete)
    
    @commands.slash_command(name="pointssub", description="To Deduct Points From Any Member.")
    async def pointssub(self, ctx, user: discord.Option(discord.Member, description="Member To Deduct Points"), points: discord.Option(int, description="Number Of Points To Deduct.")):
        await ctx.defer()
        if ctx.author != self.bot.user and ctx.author.guild_permissions.administrator == True:
            if ctx.channel.id == dataLoad.jsonDataLoader()["gsPoints"]["managePtsChannel"]:
                try:
                    currentPoints = ameydb.collection(ameydbCollection).document(str(user.id)).get().to_dict()["GameStationPoints"]
                except:
                    currentPoints = 0
                ameydb.collection(ameydbCollection).document(str(user.id)).set({ameydbCollection: f"{int(currentPoints) - int(points)}"})
                memberObject = await ctx.guild.fetch_member(user.id)
                await ctx.respond(f"{points} GameStation Points Deducted From <@{user.id}>")
                await memberObject.send(f"{points} GameStation Points Has Been Deducted From Your GameStation Account.")
            else:
                await ctx.respond(f"<@{ctx.author.id}> This Command Will Only Work In <#{dataLoad.jsonDataLoader()['gsPoints']['managePtsChannel']}>", delete_after=selfDelete)
        else: 
            await ctx.respond(f"<@{ctx.author.id}> You Don't The Permissions To Use This Command.", delete_after=selfDelete)

class checkPoints(commands.Cog, name="checkPoints"):
    def __init__(self, bot): 
        self.bot = bot
    @commands.slash_command(name="gspoints", description="To Check Your Balance Of GameStation Points.")
    async def gspoints(self, ctx):
        await ctx.defer()
        if ctx.author != self.bot.user:
            if ctx.channel.id == dataLoad.jsonDataLoader()["gsPoints"]["gsPtsChannel"]:
                try:
                    currentPoints = int(ameydb.collection(ameydbCollection).document(str(ctx.author.id)).get().to_dict()[ameydbCollection])
                except:
                    currentPoints = 0
                devName = await self.bot.fetch_user(dataLoad.jsonDataLoader()['botInfo']['devName'])
                pointsGameStationEmbed = discord.Embed(title="GameStation", color=discord.Colour.from_rgb(255, 255, 0))
                pointsGameStationEmbed.add_field(name="Your GameStation Profile", value=f"**<@{ctx.author.id}>**", inline=False)
                pointsGameStationEmbed.add_field(name="LEVEL", value=f"**{int(ameydb.collection(ameydbCollectionLvlComplete).document(str(ctx.author.id)).get().to_dict()[ameydbCollectionLvlComplete])}**", inline=True)
                pointsGameStationEmbed.add_field(name="GS POINTS", value=f"**{currentPoints}**", inline=True)
                pointsGameStationEmbed.set_thumbnail(url=ctx.author.display_avatar)
                pointsGameStationEmbed.set_footer(text=f"Developed By: {str(devName.name)}")
                await ctx.respond(embed=pointsGameStationEmbed, delete_after=selfDelete)
            else:
                await ctx.respond(f"<@{ctx.author.id}> This Command Will Only Work In <#{dataLoad.jsonDataLoader()['gsPoints']['gsPtsChannel']}>", delete_after=selfDelete)
def setup(bot):
    try:
        bot.add_cog(addPoints(bot))
        print("ManagePoints Extension Loaded")
        bot.add_cog(checkPoints(bot))
        print("CheckPoints Extension Loaded")
        bot.add_cog(levelingSystem(bot))
        print("Leveling Syetem Extension Loaded")
        bot.add_cog(errorHandler(bot))
        print("ErrorHandler Extension Loaded")
    except:
        print("Some Extensions Load Failed!")