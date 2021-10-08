import requests
from bs4 import BeautifulSoup
import pyttsx3
import datetime
from datetime import datetime
import time
import speech_recognition as sr

engine = pyttsx3.init() # voice object creation
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 155)     # setting up new voice rate
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

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

def speech(finalsplit):
    engine.say(finalsplit)
    engine.runAndWait()

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


def main ():
    command = ''
    while command is not 'power down' or 'no':
        command = listening()
        if(command == "what is the time"):
            cur_time()
        elif(command == "give me an insult"):
            insult()
        elif(command == "give me a compliment"):
            compliment()
        elif(command == 'power down' or 'no'):
            speech('goodbye')
            break
        time.sleep(3)
        speech("Is there anything else I can help with?")
       
        

main()



