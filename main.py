import requests
from bs4 import BeautifulSoup
import pyttsx3
import datetime
from datetime import datetime
import time
import speech_recognition as sr
import wolframalpha

engine = pyttsx3.init('sapi5') # voice object creation
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 155)     # setting up new voice rate
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

WAKE = "Raven"

def insult():
    URL = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    soup.get_text()
    splitword = 'insult":"'
    initalsplit = soup.get_text().partition(splitword)[2] #splits extra text before insult
    finalsplit = initalsplit.rpartition('","created"')[0] #splits extra text after insult
    speech(finalsplit)

def compliment():
    URL = "https://complimentr.com/api"
    r = requests.get(URL)   
    soup = BeautifulSoup(r.content, 'html5lib')
    soup.get_text()
    splitword = 'compliment":"'
    initalsplit = soup.get_text().partition(splitword)[2] #splits extra text before insult
    finalsplit = initalsplit.rpartition('"}')[0] #splits extra text after insult
    speech(finalsplit)

def cur_time():
    speech(("The time is now",datetime.today().strftime("%I:%M %p")))
    time.sleep(0.1)
    hour=datetime.now().hour
    if hour>=0 and hour<12:
        speech("Have a good morning")
    elif hour>=12 and hour<18:
        speech("Have a nice afternoon")
    else:
        speech("Have a good evening")

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speech("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speech("Hello,Good Afternoon")
    else:
        speech("Hello,Good Evening")

def weather():
    api_key="cb913a8dea4e3db602ff6993220e62c7"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    speech('Which city?')
    city_name = listening()
    complete_url=base_url+"appid="+api_key+"&q="+city_name
    response = requests.get(complete_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature = y["temp"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        curr_weather = (" Temperature in celcius unit is " + str(current_temperature-273.15) + "\n humidity in percentage is " + str(current_humidiy) + "\n description  " + str(weather_description))
        print(curr_weather)
        speech(curr_weather)

def wolf():
    # Taking input from user
    speech("what is your question")
    question = listening()
    # App id obtained by the above steps
    app_id = '856QLK-23G8G5KWTA'

    # Instance of wolf ram alpha
    # client class
    client = wolframalpha.Client(app_id)

    # Stores the response from
    # wolf ram alpha
    res = client.query(question)

    # Includes only text from the response
    answer = next(res.results).text
    print(answer)
    speech(answer)

def speech(finalsplit):
    # engine.say(finalsplit)
    # engine.runAndWait()
    print('qwe')

def listening():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(statement)
        except Exception as e:
            speech("Pardon me, please say that again")
            return "None"
        return statement

def wakeup():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for wake up...")
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-in')
            print('Wake up ' + statement)
        except Exception as e:
            print('No voice command')
            return "None"
        return statement

def main ():
    command = ''
    while True:
        command = wakeup()
        if command.count(WAKE) > 0:
            speech("I am ready")
            while command is not "power down" or "bye" or "no" or "goodbye":
                command = listening()
                if "time" in command:
                    cur_time()
                elif "insult" in command:
                    insult()
                elif "compliment" in command:
                    compliment()
                elif "weather" in command:
                    weather()
                elif "question" in command:
                    wolf()    
                elif "power down" or "bye" or "no" or "goodbye" in command:
                    speech('goodbye')
                    break
                time.sleep(1)
                if (command != 'power down'):
                    speech("Is there anything else I can help with?") 
     

main()



