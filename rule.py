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
        mainEmbed = discord.Embed(title="RULES", description="**Welcome to the GameStudio! We are an English-Hindi speaking server**.", color= discord.Colour.from_rgb(255, 255, 0))
        mainEmbed.add_field(name="RULE 1 - Be Civil", value="Our server is an inclusive space for our users that aligns with Discord's standards. Name-calling, racism, discrimination, and hate speech will all not be tolerated here. We want to make everyone feel welcome and be able to enjoy discussion here away from hate, and these are not conductive to that idea. Examples:", inline=False)
        mainEmbed.add_field(name="<a:arrow:928030180906237983> **Unnecessary and excessive uses of swearing against users:**", value="This refers to more abrasive language than 'fuck' or 'shit', and a word-filter is in place to automatically delete these words. Dodging this filter through text manipulation or anything similar is against this rule as well.", inline=False)
        mainEmbed.add_field(name="<a:arrow:928030180906237983> **Uses of 'kill yourself' or anything in relation to threatening a user and/or their mental state:**", value="Death threats are the most extreme form of this, and will not only result in a ban, but a report to the Discord team and the proper authorities.", inline=False)
        mainEmbed.add_field(name="<a:arrow:928030180906237983> **Discrimination and/or use of slurs against users based on:**", value="```• Race (on a basis of promoting systemic racism & overall discrimination)``````• Sexual identity (any form of LGTBQIA+ discrimination)``````• Gender identity/pronouns (any form of gender discrimination including microlabels, neopronouns, etc.)``````• Political beliefs (on a basis of marginalized groups that experience real-world discrimination, rather than fabricated)``````• Cultural groups (broader identity than Race)``````• Religious beliefs (incl. both organized/institutional and indigenous/folk religions)``````• Physical and Mental Health/Neurodivergence (including mocking the usage of tone indicators)``````• anything else undefined but still can be categorized as wanton discrimination, etc.```\n", inline=False)
        mainEmbed.add_field(name="‎", value="These forms of discrimination not only include overt statements, but also when stated as dogwhistling, or 'sarcasm'. This is a common excuse when a user breaks this rule, and is not an acceptable excuse. Comments like these, even when made in jest, reinforce the mindset in those already ascribing to such hate and vitriol. Hence, we take action to ensure that Poe's Law does not go into effect.These forms of discrimination not only include overt statements, but also when stated as dogwhistling, or 'sarcasm'. This is a common excuse when a user breaks this rule, and is not an acceptable excuse. Comments like these, even when made in jest, reinforce the mindset in those already ascribing to such hate and vitriol. Hence, we take action to ensure that Poe's Law does not go into effect.", inline=False)
        mainEmbed.add_field(name="<a:arrow:928030180906237983> **Heated arguments that result in insults:**", value="This includes for any of the discriminatory reasons above, but can generally stem from anything. It's okay to disagree with users, and fairly debate issues (not relating to above topics, i.e. debating GameStation power levels or whatnot), but if the debate results in an argument with personal attacks or devolved into in-fighting, then it breaks the rules.", inline=False)
        mainEmbed.add_field(name="<a:arrow:928030180906237983> **Do not, under any circumstances, reveal or publish personal information of any user:**", value="Doing so without consent of the individual will result in a permanent ban", inline=False)
        mainEmbed.add_field(name="<a:arrow:928030180906237983> **Do not talk ill of other users or servers:**", value="We're a big place, and are fairly interconnected with many other large pop culture communities here on Discord. Out of respect, we don't like to have gossip or screenshots from other servers taken or spoken of unknowingly without consent. There are a rare few occasions where a server's drama becomes very widespread, due to a controversy, heavy structural change, or whatnot--in these cases we will look at the topic and, provided it is relevant or important enough to be discussed/simply cannot be put down as a topic, allow it conditionally. Should such an event happen, please keep an ear out for words from the mods for directions.", inline=False)
        mainEmbed.add_field(name="<a:arrow:928030180906237983> **Unsolicited or nonconsentual venting regarding heavy topics:**", value="This means any users who may seek to talk about their problems or issues in a public context, usually of a sensitive nature. While this is certainly not a bannable offense (when not spammed), we do not want to have users discussing heavy topics that may cause grief or offense in others. If a user expresses desires of suicide or self-harm, they will be removed from the conversation temporarily and given resources to receive professional help. We allow users to discuss privately with each other to vent or discuss heavy topics, as it makes for a more consentual setting, but if a user experiences another similarly expressing thoughts of suicide or self-harm, please inform the mods right away.", inline=False)
        mainEmbed.add_field(name="<a:arrow:928030180906237983> **Be Positive about our and other communities:**", value="We'll be short in this one—don't be a fanboy and put down other fanbases. For example, 'Marvel vs DC' is a topic that serves only to be toxic and argumentative, and is rarely if ever a productive discussion. If a user frequently knocks on other communities for no valid reason, we will take action.", inline=False)
        await ctx.channel.send(embed=mainEmbed)
mainBot.run(load(open("token.json", "r"))["token"])