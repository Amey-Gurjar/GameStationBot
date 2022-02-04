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
        mainEmbed.add_field(name="**RULE 3 - No NSFW Content**", value="Here, we do not allow NSFW content of any sorts, or on any channel. This is against Discord's ruling for community servers, on top of something we do not want here in this server as well. Examples include:", inline=False)
        mainEmbed.add_field(name="<a:arrow:928030180906237983> **Explicit or otherwise pornographic content (images, videos, text etc.) in any form:**", value="This ranges from suggestive nudity, to straight up porn. Also included in this is any content not involving nudity or sex, but is made as erotic or fetish-serving content. In some rare cases, if the content is found to involve a minor or is otherwise illegal, the account will be reported to Discord and the proper authorities, on top of a ban.", inline=False)
        mainEmbed.add_field(name="<a:arrow:928030180906237983> **Content that contains gore/extreme acts of violence, abuse of people or animals, illegal acts or crimes, and anything similarly related:**", value="Generally, this content is posted for shock value, and is not permitted under any circumstances. As with any illegal acts in pornographic content, the account will be reported to Discord and the proper authorities, on top of a ban.", inline=False)
        mainEmbed.add_field(name="<a:arrow:928030180906237983> **Unsolicited messages both in the server and in DM messages in a sexual context:**", value="This includes users talking excessively about their sexual desires or general sexual content in the server's channels, but goes beyond us as well. We take steps to protect our users from any who privately message them to sext, send inappropriate content, seek roleplaying for fetish reasons, desire unsolicited relationships/date, or in some extreme cases, grooming if the targeted user is a minor. As always, we advise personal vigilance to our userbase for recognizing the signs of a predatory user when it occurs, and to report any events to our mod team. Our mod team has (regrettably) had much experience in dealing with these predators and groomers, and we are here to help you in the event this happens to you. Any of these offenses against a minor will result, as always, in a report to both Discord and the proper authorities.", inline=False)
        await ctx.channel.send(embed=mainEmbed)
mainBot.run(load(open("token.json", "r"))["token"])