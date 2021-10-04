import pyttsx3                       #https://www.youtube.com/watch?v=BwkwwxPHeSU
                                     #https://pyttsx3.readthedocs.io/en/latest/engine.html







engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices') #pick a voice from the list mail and female verison
engine.setProperty('voice',voice[1].id) #from the voice list select the type 0 for male and 1 for female
rate = engine.getProperty('rate') 
engine.setProperty('rate', rate-10) #make the voice  slower 
#function that speak out 

def sperak(audio):
    engine.say(audio) #speak the audio 
    engine.runAndWait() #Wait while running the speech 


#sperak("hello this is the first test ")