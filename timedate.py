import datetime
import requests
from dotenv import load_dotenv
import os 

def configure():
    load_dotenv()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        return("Hello,Good Morning")
    elif hour>=12 and hour<18:
        return("Hello,Good Afternoon")
    else:
        return("Hello,Good Evening")
    
def cur_time():
    now=  datetime.datetime.now()
    cur = ("The time is now",now.strftime("%H:%M"))
    if now.hour >= 0 and now.hour < 12:
        greeting = "Have a good morning"
    elif now.hour >= 12 and now.hour < 18:
        greeting = "Have a nice afternoon"
    else:
        greeting = "Have a good evening"
    return cur, greeting

def cur_weather():
    configure()
    api = f"https://api.openweathermap.org/data/2.5/weather?q=Montego Bay&&appid={os.getenv('api_key')}"
    response = requests.get(api)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature = y["temp"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        curr_weather = ("Temperature is " + str(round(current_temperature-273.15)) + " degrees celcius " + "with " + str(current_humidiy) + " humidity and "+ "with " + str(weather_description))
        return curr_weather