import pyttsx3  # https://www.youtube.com/watch?v=BwkwwxPHeSU #https://pyttsx3.readthedocs.io/en/latest/engine.html
import datetime as datetime
import speech_recognition as sr  # https://realpython.com/python-speech-recognition/
import sys 
from settings import Settings


class Assistant():
    def __init__(self):
        self.r = sr.Recognizer()  # This is recognizer class
        self.settings = Settings()
        self.engine = pyttsx3.init('sapi5')
        # pick a voice from the list mail and female verison
        self.voice = self.engine.getProperty('voices')
        # from the voice list select the type 0 for male and 1 for female
        self.engine.setProperty('voice', self.voice[self.settings.voice_type].id)
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate',self.settings.voice_rate)  # make the voice  slower
        # function that speak out




    def speak(self, audio):
        """function that will speak out a given sentence """

        self.engine.say(audio)  # speak the audio
        self.engine.runAndWait()  # Wait while running the speech





    def takecmd(self):
        """this function for taking  voice command """

        with sr.Microphone() as source:  # activate Mirophone as a input scource
            self.speak("lesening .... ")
            self.r.phrase_threshold = 1  # wait command for 1 second to take command
            audio = self.r.listen(source=source)
        try:
            print("Recognizing ....")
            # convert the audio into text
            query = self.r.recognize_google(audio, language='en-in')
            print(f'user said {query}')
        except Exception as e:
            print(e)
            self.speak("faceing some problem to recognize")
            return "None"

        return query






if __name__ == '__main__':
    p=Assistant()
    p.speak("hello everyone this is a test")
    p.takecmd()
#sperak("hello this is the first test ")
