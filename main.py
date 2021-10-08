#https://public-apis.io/evil-insult-generator-api
#https://complimentr.com/
#https://m3o.com/
from typing import final
import requests
from bs4 import BeautifulSoup
import pyttsx3

engine = pyttsx3.init() # object creation

def insult():
    URL = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    soup.get_text()
    splitword = 'insult":"'
    initalsplit = soup.get_text().partition(splitword)[2] #splits extra text before insult
    finalsplit = initalsplit.rpartition('","created"')[0] #splits extra text after insult
    speech(finalsplit)

def speech(finalsplit):
    print('this')
    engine.say(finalsplit)
    engine.runAndWait()

def main ():
    insult()

main



