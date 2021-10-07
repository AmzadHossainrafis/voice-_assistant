import wikipedia
import webbrowser
from voice_assi import Assistant



class Wiki():
    def __init__(self):
        self.VA= Assistant()
        self.settings = self.VA.settings


    def wiki(self,query):
        self.VA.speak("Searching wikipedia..")
        replace=query.replace("wikipedia","")
        result=wikipedia.summary(replace)
        self.VA.speak("according to wikipedia")
        print(result)
        self.VA.speak(result)


    def brow_(self,query):
        # t=self.VA.takecmd()
        replace=query.replace("browse","")
        self.VA.speak(f'visiting {replace}')
        webbrowser.open(replace)
        

if __name__ == '__main__':
    a=Wiki()
    a.brow_()

        
