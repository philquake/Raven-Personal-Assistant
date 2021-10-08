#https://public-apis.io/evil-insult-generator-api
#https://complimentr.com/
#https://m3o.com/
from typing import final
import requests
from bs4 import BeautifulSoup
import pyttsx3

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

def speech(finalsplit):
    print('this')
    engine.say(finalsplit)
    engine.runAndWait()

def main ():
    #insult()
    compliment()

main()



