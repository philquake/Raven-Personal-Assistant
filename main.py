#https://public-apis.io/evil-insult-generator-api
#https://complimentr.com/
#https://m3o.com/
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import os
from requests.structures import CaseInsensitiveDict

def insult():
    URL = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    soup.get_text()
    # print(soup.get_text())
    # print(soup.get_text().split('insult":"'))
    splitword = 'insult":"'
    initalsplit = soup.get_text().partition(splitword)[2] #splits extra text before insult
    finalsplit = initalsplit.rpartition('","created"')[0] #splits extra text after insult
    tts(finalsplit)

def compliment():
    URL = "https://complimentr.com/api"
    r = requests.get(URL)   
    soup = BeautifulSoup(r.content, 'html5lib')
    soup.get_text()
    splitword = 'compliment":"'
    initalsplit = soup.get_text().partition(splitword)[2] #splits extra text before insult
    finalsplit = initalsplit.rpartition('"}')[0] #splits extra text after insult
    tts(finalsplit)

def tts(finalsplit):
    language = 'en'
    myobj = gTTS(text=finalsplit, lang=language, slow=False)
    myobj.save("audio.mp3")
    os.system("start audio.mp3")

def current_weather():
    url = "https://api.m3o.com/v1/weather/Forecast"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = "Bearer MzdjNDlmZmUtNGMxOC00MGI2LWE3NTEtNDQwYTYzNWI3YzRl"

    data = """    {    "location": "Jamaica"    }    """

    r = requests.post(url, headers=headers, data=data)
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
    print(soup.prettify())
    splitword = 'max_temp_f":'
    asplit = soup.get_text().partition(splitword)[2] #splits extra text before insult
    tempf = asplit.rpartition(',"min_temp_c')[0]
    print(tempf)

def main():
    # insult()
    # compliment()
    current_weather()
    

main()
