
import datetime as datetime
from voice_assi import Assistant


class DateandTime():
    def __init__(self):
        self.VA = Assistant()
        self.settings = self.VA.settings

    def greeting(self):
        """this function find out time and greet you accordingly """

        hour = int(datetime.datetime.now().hour)  # just bring out the hour
        if hour >= 0 and hour < 12:
            self.VA.speak("Good Morning Sir !")

        elif hour >= 12 and hour < 18:
            self.VA.speak("Good Afternoon Sir !")

        else:
            self.VA.speak("Good Evening Sir !")
        # self.VA.speak(" I am your voice assistant ")
        # self.VA.speak("how can i help you ")
    

    def time(self):
        
        hour=datetime.datetime.today().strftime("%I:%M %p")
        # minute=datetime.datetime.now().minute
        query=f'the time is {hour}'
        self.VA.speak(query)

    def date(self):
        date=datetime.datetime.today().strftime("%Y,%b")
        query=f"today's date is{date} "
        self.VA.speak(query)


# if __name__ == '__main__':
#     # a=DateandTime()
#     # a.date()
#     # # a.time()
#     # # a.greeting()


        
