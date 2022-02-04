from json import load
from urllib.request import urlopen
import requests
def weather(location):
        BASE_URL = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid=9834d7f1a59251031184ca2922593739"
        response = requests.get(BASE_URL)
        try:
            if response.status_code == 200:
                data = response.json()
                main = data['main']
                temperature = main['temp']
                report = data['weather']
                temp = f"{(int(temperature))}"
                report = f"{report[0]['description']}"
                weatherFinal = f"In {location.title()}, It's {temp} Degrees Celcius With {report.title()}"
                print(weatherFinal)
        except Exception as e:
            print(e)
weather("borivali")