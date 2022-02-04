from discord.ext import commands
import discord
from json import load
from urllib.request import urlopen
import requests
from random import choice
selfDelete = 12.0
class mainWeatherBot(commands.Cog, name="mainWeatherBot"):
    global dataJson
    def __init__(self, bot):
        self.bot = bot
    def dataJson():
        mainData = load(open("mainData.json", "r"))
        return mainData
    @commands.slash_command(name="weather", description="Shows The Weather")
    async def weather(self, ctx, city: discord.Option(str, description="City Of Which The Weather You Want")):
        await ctx.defer()
        try:
            mainWeatherData = load(urlopen(f"http://api.openweathermap.org/data/2.5/weather?q={city.replace(' ', '+')}&units=metric&appid=9834d7f1a59251031184ca2922593739"))
            weatherSlang = ["Right Now In", "In", "Currently In", "Today In"]
            main = mainWeatherData['main']
            temp = f"{(int(main['temp']))}"
            report = f"{mainWeatherData['weather'][0]['description']}"
            weatherEmbed = discord.Embed(title="GameStation Weather", color=discord.Color.from_rgb(255, 255, 0))
            weatherEmbed.add_field(name=f"{choice(weatherSlang)} {city.title()},", value=f"**It's {temp}° Celcius With {report.title()}**")
            for weatherReport in list(dataJson()["weatherData"].keys()):
                for i in range(len(report.split())):
                    if report.split()[i].lower() in weatherReport.lower():
                        weatherEmbed.set_image(url=dataJson()["weatherData"][weatherReport])
            await ctx.send_followup(embed=weatherEmbed, delete_after=selfDelete)
        except:
            await ctx.send_followup("Sorry City Not Found!", delete_after=selfDelete)
def setup(bot):
    bot.add_cog(mainWeatherBot(bot))