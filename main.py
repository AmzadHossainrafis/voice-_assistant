from voice_assi import Assistant
from dateandtime import DateandTime
from email1 import MailandCont
from Rnotification import Rm
from browsing import Wiki
from Weatheandnews import weatherandNews
from browsing import Wiki

class main():
    def __init__(self):
        self.VA=Assistant()
        self.setting=self.VA.settings 
        self.DT=DateandTime()
        self.DT.greeting()
        del self.DT



    def run(self):
        self.runing= True
        while self.runing:
            speach=self.VA.takecmd().lower()
            if "date" in speach:
                self.obj=DateandTime()
                speak=self.obj.date()
                self.VA.speak(speak)
                del self.obj

            elif "time" in speach:
                self.obj=DateandTime()
                speak=self.obj.time()
                self.VA.speak(speak)
                del self.obj

            elif "weather" in speach:
                self.weather=weatherandNews()
                self.weather.weather('Dhaka')
                del self.weather

            elif "news" in speach:
                self.weather=weatherandNews()
                self.weather.news()
                del self.weather
            
            elif "mail" in speach:
                pass
            elif "wikipedia" in speach:
                self.brw=Wiki()
                self.brw.wiki(speach)
                del self.brw
            elif "browse" in speach:
                self.brw=Wiki()
                self.brw.brow_(speach)
                del self.brw
            elif "google search" in speach:
                self.brw=Wiki()
                self.brw.google_search_(speach)
                del self.brw

            elif "set reminder" in speach:
                self.RMD=Rm()
                self.RMD.writenote()
                del self.RMD
            elif "read reminder" in speach:
                self.RMD=Rm()
                self.RMD.readnote('data/note')
                del self.RMD

            elif "notfy me" in speach:
                self.RMD=Rm()
                self.VA.speak("what is the titale ")
                x=self.VA.takecmd().lower()
                self.VA.speak("what is the message")
                y=self.VA.takecmd().lower()
                self.VA.speak("when you want the notification")
                z=self.VA.takecmd().lower()
                # convert the time 

            elif "send mail " in speach:
                self.VA.speak(" to who you wanna send mail ")
                name=self.VA.takecmd().lower()
                self.mail=MailandCont(name)
                self.mail.sendmail()
                self.VA.speak("what you want to say")
                msgg=self.VA.takecmd()
                self.mail.sendmail(msg=msgg)
                del self.mail
            elif " tell me a joke" in speach:
                self.joke=Wiki()
                r=self.joke.get_jokes()
                self.VA.speak(r)
                del self.joke





                




            else:
                continue




            




if __name__ == '__main__':
    test=main()
    test.run()








