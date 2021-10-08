import requests
from bs4 import BeautifulSoup
import pyttsx3
import datetime
from datetime import datetime
import time

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

def main ():
    #insult()
    #compliment()
    #wishMe()
    cur_time()

main()



