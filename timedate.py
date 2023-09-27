import datetime
import requests

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
        hour = "Have a good morning"
    elif now.hour >= 12 and now.hour < 18:
        hour = "Have a nice afternoon"
    else:
        hour = "Have a good evening"
    return cur, hour

def weather(city):
    api_key="cb913a8dea4e3db602ff6993220e62c7"
    base_url="https://api.openweathermap.org/data/2.5/weather?" 
    complete_url=base_url+"appid="+api_key+"&q="+city
    response = requests.get(complete_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature = y["temp"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        curr_weather = ("Temperature is " + str(current_temperature-273.15) + " celcius " + "with " + str(current_humidiy) + " humidity and "+ "with " + str(weather_description))
        return curr_weather