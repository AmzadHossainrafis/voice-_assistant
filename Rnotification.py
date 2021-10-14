from plyer import notification 
import datetime as datetime
from settings import Settings
from voice_assi import Assistant

class Rm():

    def __init__(self):
        self.VA=Assistant()
        self.settings=Settings()

    def notfy(self,title,message,timout ):
        notification.notify(title=title,message=message,app_icon=None,timout=10)

    def writenote(self):
        self.VA.speak("what is the note title")
        title=self.VA.takecmd()
        self.VA.speak(" what is you note ")
        message=self.VA.takecmd()
        date=datetime.datetime.today().strftime("%Y,%b")
        with open(self.settings.note_dir,"w") as f:

            f.write(f'date :{str(date)}\n')
            f.write(f" titele :{str(title)}\n")
            f.write(f' message :{str(message)}')
            f.close()
        self.VA.speak(" note taken ")



    def readnote(self,filenam):
        with open(f"{filenam}.txt","r") as f:
            read=f.read()
            print(read)
        self.VA.speak(read)

   
   # writenote(title="this is a test_title",message=" remaind me to call abba and amma ")
if __name__ == '__main__':
    test=Rm()
    test.writenote()
    test.readnote(str("data/note"))