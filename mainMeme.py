import discord
from discord.ext import commands
from threading import Thread
from PIL import Image
from io import BytesIO
from urllib.request import urlopen
from json import load
import requests
import os
GameBotData = []
class MemeData(Thread):
    def dataFetch():
        dataJson = load(open("mainData.json", "r"))
        return  dataJson    
class ImageManupulation(Thread):
    async def imageMeme(ctx, user, imageName, imageNameFinal, imageSize, authorAvatar, userAvatar):
        if user == None:
            user = ctx.author
        mainImage = Image.open(urlopen(imageName)).convert("RGBA")
        authorImageFinal = Image.open(BytesIO(await ctx.author.display_avatar.read()))
        userImageFinal = Image.open(BytesIO(await user.display_avatar.read()))
        authorImageFinal = authorImageFinal.convert("RGBA").resize(imageSize)
        userImageFinal = userImageFinal.convert("RGBA").resize(imageSize)
        mainImage.paste(authorImageFinal, authorAvatar)
        mainImage.paste(userImageFinal, userAvatar)
        mainImage.save(imageNameFinal, format="png")
        await ctx.send_followup(file=discord.File(imageNameFinal))
        os.remove(imageNameFinal)  
    async def imageGay(ctx, user, imageName, imageNameFinal, imageSize):
        if user == None:
            user = ctx.author
        mainImage = Image.open(urlopen(imageName)).convert("RGBA")
        avatarImage = Image.open(BytesIO(await user.display_avatar.read()))
        avatarImage = avatarImage.convert("RGBA").resize(imageSize)
        mainImage = mainImage.convert("RGBA").resize(imageSize)
        Image.blend(avatarImage, mainImage, 0.5).save(imageNameFinal, format="png")
        await ctx.send_followup(file=discord.File(imageNameFinal))
        os.remove(imageNameFinal)
    async def imageUser(ctx, user, imageName, imageNameFinal, imageSize, userAvatar):
        if user == None:
            user = ctx.author
        mainImage = Image.open(urlopen(imageName)).convert("RGBA")
        userImageFinal = Image.open(BytesIO(await user.display_avatar.read()))
        userImageFinal = userImageFinal.convert("RGBA").resize(imageSize)
        mainImage.paste(userImageFinal, userAvatar)
        mainImage.save(imageNameFinal, format="png")
        await ctx.send_followup(file=discord.File(imageNameFinal))
        os.remove(imageNameFinal)
class memeSystem(commands.Cog, name="memeSystem"):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(name="meme", description="To Send Randon Meme")
    async def meme(self, ctx):
        await ctx.defer()
        memeRequest = requests.get("https://memes.blademaker.tv/api?lang=en")
        memeRequest = memeRequest.json()
        memeTitle = memeRequest["title"]
        memeUps = memeRequest["ups"]
        memeDowns = memeRequest["downs"]
        memeSub = memeRequest["subreddit"]
        memeEmded = discord.Embed(title=f"{memeTitle}")
        memeEmded.set_image(url = memeRequest["image"])
        memeEmded.set_footer(text=f"👍{memeUps} 👎{memeDowns}")
        await ctx.send_followup(embed=memeEmded)
    @commands.slash_command(name="imageslap", description="To Meme A User To Slap")
    async def imageslap(self, ctx, user: discord.Option(discord.Member, description="User To Slap", required=False, default=None)):
        await ctx.defer()
        await ImageManupulation.imageMeme(ctx=ctx, user=user, imageName=MemeData.dataFetch()["memeData"]["slapImage"], imageNameFinal="finalSlap.png", imageSize=(275, 275), authorAvatar=(512, 112), userAvatar=(860, 335))
    @commands.slash_command(name="imagegay", description="Make The User Gay")
    async def imagegay(self, ctx, user: discord.Option(discord.Member, description="User To Make Gay", required=False, default=None)):
        await ctx.defer()
        await ImageManupulation.imageGay(ctx=ctx, user=user, imageName=MemeData.dataFetch()["memeData"]["gayImage"], imageNameFinal="gayFinal.png", imageSize=(300, 300))
    @commands.slash_command(name="imagedelete", description="Delete Someone")
    async def imagedelete(self, ctx,  user: discord.Option(discord.Member, description="User To Delete", required=False, default=None)):
        await ctx.defer()
        await ImageManupulation.imageUser(ctx=ctx, user=user, imageName=MemeData.dataFetch()["memeData"]["deleteImage"], imageNameFinal="deleteFinal.png", imageSize=(400, 400), userAvatar=(335, 300))
def setup(bot):
    bot.add_cog(memeSystem(bot))
    print("MemeEngine started")