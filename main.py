from misc import *
from timedate  import *
import time

import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5') # voice object creation
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 155)     # setting up new voice rate
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)  #changing index, changes voices. 1 for female

WAKE = 'Raven'

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

def wakeup():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for wake up...")
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-in')
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
            while command != "power down":
                command = listening()
                if "time" in command:
                    cur_time()
                elif "insult" in command:
                    insult()
                elif "compliment" in command:
                    compliment()
                elif "weather" in command:
                    cur_weather()  
                elif "power down" in command:
                    speech('goodbye')
                    break
                time.sleep(10)
                if (command != 'power down'):
                    speech("Is there anything else I can help with?") 
 
     

speech(cur_weather)