from discord.ext import commands
from discord.ui import Button, View
import discord
from threading import Thread
from json import load
import asyncio
from random import randint, choice
mainDataJson = "mainData.json"
selfDelete = 10.0
spamLimit = 4
afkMembers = {}
messageSpamList = {}
class mainFunc(Thread):
    global dataJson, gameTypeOption
    def dataJson():
        mainData = load(open(mainDataJson, "r"))
        return mainData
class readyBot(commands.Cog, name="readyBot"):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        mainGuild = self.bot.get_guild(load(open("token.json"))["guild"][0])
        mainChannel = mainGuild.get_channel(dataJson()["serverChannels"]["systemLogs"])
        await mainChannel.send(f"GameStation Is Running...")
        print(f"GameStation Is Running")
class welcomeBot(commands.Cog, name="welcomeBot"):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.bot == False:
            mainChannel = member.guild.get_channel(dataJson()["serverChannels"]["welcomeChannel"])
            botDev = await self.bot.fetch_user(dataJson()["botInfo"]["devName"])
            welcomeEmbed = discord.Embed(title=f"{member.guild.name}", description=f"Hello <@{member.id}>,\nWelcome To The {member.guild.name}", color=discord.Colour.from_rgb(255, 255, 0))
            welcomeEmbed.add_field(name="Game Roles", value=f"Take Your Game Roles <#{dataJson()['serverChannels']['gameRoles']}>")
            welcomeEmbed.add_field(name="Rules", value=f"Read The Server Rules <#{dataJson()['serverChannels']['rulesChannel']}>")
            welcomeEmbed.add_field(name="Chat", value=f"Chat Here In <#{dataJson()['serverChannels']['generalChat']}>")
            welcomeEmbed.set_thumbnail(url=member.display_avatar)
            welcomeEmbed.set_image(url=dataJson()["embedOption"]["welcomeGif"])
            welcomeEmbed.set_footer(text=f"Developed By: {botDev.name}")
            await mainChannel.send(embed=welcomeEmbed)
class gameRoles(commands.Cog, name="gameRoles"):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_interaction(self, interaction):
        if interaction.user.bot == False:
            if interaction.type == discord.InteractionType.component:
                if interaction.message.id == dataJson()["serverChannels"]["gameRolesMessage"]:
                    for role in range(len(dataJson()["gameRoles"])):
                        if interaction.data["custom_id"] == list(dataJson()["gameRoles"].keys())[role]:
                            mainRole = interaction.guild.get_role(list(dataJson()["gameRoles"].values())[role])
                            if mainRole not in interaction.user.roles:
                                await interaction.user.add_roles(mainRole)
                                await interaction.response.defer()
                            else:
                                await interaction.user.remove_roles(mainRole)
                                await interaction.response.defer()                
class spamBot(commands.Cog, name="spamBot"):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author.bot == False and ctx.channel.type != discord.ChannelType.private and ctx.channel.type != discord.ChannelType.private:
            discord.Message
            mainRole = ctx.guild.get_role(int(dataJson()["botInfo"]["adminRole"]))
            if mainRole not in ctx.author.roles:
                userMessage = ctx.content
                for i in dataJson()["bannedWords"]:
                    if i in userMessage:
                        await ctx.delete()
                        await ctx.channel.send(f"{ctx.author.mention} Don't Abuse!", delete_after=selfDelete)
                userMessageList = ctx.content.split(" ")
                for i in range(len(userMessageList)):
                    wordcount = 1
                    for j in range(i + 1, len(userMessageList)):
                        if userMessageList[i] == (userMessageList[j]):
                            wordcount = wordcount + 1
                    if wordcount > int(spamLimit):
                        await ctx.delete()
                        await ctx.channel.send(f"{ctx.author.mention} Don't Spam!", delete_after=selfDelete)
                if ctx.author.id not in messageSpamList:
                    messageSpamList.update({ctx.author.id: []})
                    messageSpamList[ctx.author.id].append(userMessage)
                    if len(messageSpamList[ctx.author.id]) > (int(spamLimit)):
                        messageSpamList[ctx.author.id].pop(0)
                    if messageSpamList[ctx.author.id].count(userMessage) > spamLimit:
                        await ctx.channel.purge(limit=messageSpamList[ctx.author.id].count(userMessage))
                        messageSpamList.pop(ctx.author.id)
                        await ctx.channel.send(f"{ctx.author.mention} Don't Spam!", delete_after=selfDelete) 
    @commands.slash_command(name="clear")
    async def clear(self, ctx, clearnum: discord.Option(int, description="Number Of Messages To Clear")):
        mainRole = ctx.guild.get_role(int(dataJson()["botInfo"]["adminRole"]))
        if mainRole in ctx.author.roles:
            await ctx.respond("‎", delete_after=0.0)
            await ctx.channel.purge(limit=clearnum)
            await ctx.channel.send(f"{clearnum} Messages Cleared!", delete_after=selfDelete)
        else:
            await ctx.respond("You Don't Have Permissions!", delete_after=selfDelete)
class mainBot(commands.Cog, name="mainBot"):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(name="invite", description="Invite Players To Game") 
    async def invite(self, ctx, gametype: discord.Option(str)):
        gameChannels = dataJson()["gameChannels"]
        for channel in range(len(gameChannels)):
            if ctx.channel.id == list(gameChannels.values())[channel]:
                mainRole = ctx.guild.get_role(int(list(dataJson()['gameRoles'].values())[channel]))
                randomColor = [randint(0, 255), randint(0, 255), randint(0, 255)]
                mainEmbed = discord.Embed(title=f"{list(gameChannels.keys())[channel]} Invite", color=discord.Colour.from_rgb(randomColor[0], randomColor[1], randomColor[2]))
                mainEmbed.add_field(name=f"{gametype.title()} Game", value=f"**<@&{list(dataJson()['gameRoles'].values())[channel]}>\n{ctx.author.mention} Is Inviting You For A {gametype.title()} Game**", inline=False)
                mainEmbed.set_image(url=choice(load(open("mainData.json"))["gameContent"][list(gameChannels.keys())[channel]]["embedGif"]))
                await ctx.respond("‎", delete_after=0.0)
                await ctx.channel.send(mainRole.mention, embed=mainEmbed)
class afkBot(commands.Cog, name="afkBot"):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(name="afkadd", description="To Become AFK")
    async def afkadd(self, ctx, reason: discord.Option(str, "AFK REASON", required=False, default=None)):
        await ctx.defer()
        if ctx.author.bot == False and ctx.channel.type != discord.ChannelType.private:
            if ctx.author.id not in list(afkMembers.keys()):
                afkMembers.update({ctx.author.id: reason})
                await ctx.send_followup(f"<@{ctx.author.id}> Now You Are AFK.", delete_after=selfDelete)
            else:
                await ctx.send_followup(f"<@{ctx.author.id}> You Are Already AFK.", delete_after=selfDelete)
        else:
            await ctx.send_followup(f"‎", delete_after=0.0)
    @commands.slash_command(name="afkremove", description="To Remove AFK")
    async def afkremove(self, ctx):
        await ctx.defer()
        if ctx.author.bot == False and ctx.channel.type != discord.ChannelType.private:
            if ctx.author.id in list(afkMembers.keys()):
                afkMembers.pop(ctx.author.id)
                await ctx.send_followup(f"<@{ctx.author.id}> AFK Removed.", delete_after=selfDelete)
            else:
                await ctx.send_followup(f"<@{ctx.author.id}> You Are Not AFK.", delete_after=selfDelete)
    @commands.Cog.listener()
    async def on_message(self, ctx):
        for mention in ctx.mentions:
            if mention.id in afkMembers and ctx.author.bot == False:
                await ctx.channel.send(f"<@{ctx.author.id}>, <@{mention.id}> Is Busy Right Now.\nReason: {afkMembers[mention.id]}", delete_after=selfDelete)
class kickBan(commands.Cog, name="kickBan"):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(name="kick", description="Kicks The User Mentioned")
    async def kick(self, ctx, user: discord.Option(discord.Member, description="User To Kick"), reason: discord.Option(str, description="Reason For The Kick", required="False", default="Not Mentioned")):
        await ctx.defer()
        if ctx.author.guild_permissions.administrator == True:
            try:
                await user.send(f"You Have Been Kicked From {ctx.guild.name} By <@{ctx.author.id}>\nReason: {reason}")
            except: pass
            await user.kick()
            await ctx.send_followup(f"<@{user.id}> Was Kicked By <@{ctx.author.id}>\nReason: {reason}")
        else:
            await ctx.send_followup(f"<@{ctx.author.id}> You Don't Have Permissions To Use This!")
    @commands.slash_command(name="ban", description="Bans The User Mentioned")
    async def ban(self, ctx, user: discord.Option(discord.Member, description="User To Ban"), reason: discord.Option(str, description="Reason For The Ban", required=False, default="Not Mentioned")):
        await ctx.defer()
        if ctx.author.guild_permissions.administrator == True:
            try:
                await user.send(f"You Have Been Banned From {ctx.guild.name} By <@{ctx.author.id}>\nReason: {reason}")
            except: pass
            await user.ban()
            await ctx.send_followup(f"<@{user.id}> Was Banned By <@{ctx.author.id}>\nReason: {reason}")
        else:
            await ctx.send_followup(f"<@{ctx.author.id}> You Don't Have Permissions To Use This!")
    @commands.slash_command(name="unban", description="Unbans The User Mentioned")
    async def unban(self, ctx, user: discord.Option(discord.Member, description="User To Unban"), reason: discord.Option(str, description="Reason For The Unban", required=False, default="Not Mentioned")):
        await ctx.defer()
        if ctx.author.guild_permissions.administrator == True:
            banned_users = await ctx.guild.bans()
            userObject = await self.bot.fetch_user(user)
            user_name, user_tag = str(userObject).split("#")
            for ban_user in banned_users:
                if ban_user.user.id == user:
                    memberBanned = ban_user.user
                else:
                    await ctx.send_followup(f"<@{ctx.author.id}>, <@{userObject.id}> Is Not Banned!")
                    return None
            if (memberBanned.name, memberBanned.discriminator) == (user_name, user_tag):
                await ctx.guild.unban(memberBanned)
                try:
                    await memberBanned.send(f"You Are Unbanned From {ctx.guild.name} By <@{ctx.author.id}>\n Reason: {reason}")
                except: pass
                await ctx.send_followup(f"<@{memberBanned.id}> Was Unbanned By <@{ctx.author.id}>\n Reason: {reason}")
            else:
                await ctx.send_followup(f"<@{ctx.author.id}>, <@{user.id}> Is Not Banned!")
        else:
            await ctx.send_followup(f"<@{ctx.author.id}> You Don't Have Permissions To Use This!")
class warnBot(commands.Cog, name="warnBot"):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(name="warn", description="To Warn A Member")
    async def warn(self, ctx, user: discord.Option(discord.Member), reason: discord.Option(str, required=False, default="Not Mentioned"), time: discord.Option(int, description="Mute Time In Sec.", required=False, default=0)):
        await ctx.defer()
        if ctx.author.guild_permissions.administrator == True: 
            permit = ctx.channel.overwrites_for(user)
            await ctx.channel.set_permissions(user, send_messages=False)
            await ctx.send_followup(f"<@{user.id}> You Are Warned. Reason: {reason}. Time: {time} Seconds.")
            await asyncio.sleep(time)
            await ctx.channel.set_permissions(user, send_messages=True)
        else:
            await ctx.send_followup(f"<@{ctx.author.id}> You Don't Have Permissions To Use This!")
def setup(bot):
    bot.add_cog(readyBot(bot))
    bot.add_cog(welcomeBot(bot))
    bot.add_cog(gameRoles(bot))
    bot.add_cog(spamBot(bot))
    bot.add_cog(mainBot(bot))
    bot.add_cog(afkBot(bot))
    bot.add_cog(kickBan(bot))
    bot.add_cog(warnBot(bot))