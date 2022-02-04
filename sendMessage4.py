from discord import Bot
import discord
from json import load
mainIntents = discord.Intents.default()
mainIntents.members = True
mainIntents.presences = True
mainBot = Bot(debug_guilds=load(open("token.json"))["guild"], activity=discord.Activity(type=discord.ActivityType.watching, name=f"GameStation"), intents=mainIntents, status=discord.Status.dnd)

@mainBot.event 
async def on_message(ctx):
    if ctx.author != mainBot.user:
        mainEmbed = discord.Embed(color= discord.Colour.from_rgb(255, 255, 0))
        mainEmbed.add_field(name="**RULE 4 - No Piracy**", value="Although discussion of piracy is allowed to an extent*, any naming of illegal sites, direct links to unofficial streams and downloads (including in-Discord screen sharing), or advising others on how to stream or download pirated content, is not allowed. We understand people's frustrations when relevant content is not allowed in their country or is otherwise not available, or is otherwise unaccessible to them.\nHowever, we cannot permit that content here, as it is against Discord's Terms of Service and standards of a community server\n*If the topic arises, please first ask a moderator to allow discussion.", inline=False)
        mainEmbed.set_image(url="https://cdn.discordapp.com/attachments/902611609241944134/925305161189052436/new_rules_banner.png")
        await ctx.channel.send(embed=mainEmbed)
mainBot.run(load(open("token.json", "r"))["token"])