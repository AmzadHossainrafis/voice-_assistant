import pyttsx3                       #https://www.youtube.com/watch?v=BwkwwxPHeSU
                                    #https://pyttsx3.readthedocs.io/en/latest/engine.html
import datetime as datetime






engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices') #pick a voice from the list mail and female verison
engine.setProperty('voice',voice[1].id) #from the voice list select the type 0 for male and 1 for female
rate = engine.getProperty('rate') 
engine.setProperty('rate', rate-20) #make the voice  slower 
#function that speak out 

def speak(audio):
    engine.say(audio) #speak the audio 
    engine.runAndWait() #Wait while running the speech 
def greeting():
    hour =int(datetime.datetime.now().hour) #just bring out the hour 
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")  
  
    else:
        speak("Good Evening Sir !") 
    speak(" I am your voice assistant ")

greeting()

#sperak("hello this is the first test ")