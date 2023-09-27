import requests
from bs4 import BeautifulSoup

def insult():
    URL = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    splitword = 'insult":"'
    initalsplit = soup.get_text().partition(splitword)[2] #splits extra text before insult
    finalsplit = initalsplit.rpartition('","created"')[0] #splits extra text after insult
    return finalsplit

def compliment():
    URL = "https://8768zwfurd.execute-api.us-east-1.amazonaws.com/v1/compliments"
    r = requests.get(URL)   
    soup = BeautifulSoup(r.content, 'html5lib')
    # splitword = ""
    # initalsplit = soup.get_text().partition(splitword)[2] #splits extra text before insult
    # finalsplit = initalsplit.rpartition('"}')[0] #splits extra text after insult
    return(soup.get_text())