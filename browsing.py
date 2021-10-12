import wikipedia
import webbrowser
from voice_assi import Assistant



class Wiki():
    """this class will  browse web and search web and also can make wiki summary"""
    def __init__(self):
        self.VA= Assistant()  #Assistant object 
        self.settings = self.VA.settings #taking satting 


    def wiki(self,query):
        """ wiki search and make summary """

        self.VA.speak("Searching wikipedia..")
        replace=query.replace("wikipedia","")
        result=wikipedia.summary(replace)
        self.VA.speak("according to wikipedia")
        print(result)
        self.VA.speak(result)


    def brow_(self,query):
        """web search and browsing """
        # t=self.VA.takecmd()
        replace=query.replace("browse","www.")
        self.VA.speak(f'visiting {replace}')
        webbrowser.open(replace)
        

# if __name__ == '__main__':
#     # a=Wiki()
#     # a.wiki("cristiano ronaldo")

        
