import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5') # voice object creation
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 155)     # setting up new voice rate
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)  #changing index, changes voices. 1 for female


engine = pyttsx3.init()


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

def main():
    # speech("hello there stranger")
    listening()

main ()
