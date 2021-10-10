import requests
from settings import Settings
from voice_assi import Assistant
import datetime as datetime


class weatherandNews():
    def __init__(self):
        self.settings = Settings()
        self.VA= Assistant()
        self.api_key=self.settings.wkey
        self.new_api_link=self.settings.new_key


    def weather(self,city_name):
        self.api_link=f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={self.api_key}"
        print(self.api_link)
        self.api_req=requests.get(self.api_link)
        self.api_data=self.api_req.json()
        
        print(self.api_data)

        if self.api_data["cod"]=="404":
            print('having problem to get the data')
        else:
            self.tem=((self.api_data['main']['temp'])-273.15)
            self.VA.speak(f"the weathe of {city_name} is {round(self.tem)} degree")
    
    def news(self,subject):
        date=datetime.datetime.today().strftime("%Y-%M-%d")
        self.test=f'https://newsapi.org/v2/everything?domains=techcrunch.com,thenextweb.com&apiKey={self.new_api_link}'
        self.newapi=f'https://newsapi.org/v2/everything?q={subject}&from={date}&sortBy=popularity&apiKey={self.new_api_link}'
        self.new_req=requests.get(self.test)
        self.new_data=self.new_req.json()
        self.result=[]

        self.artical=self.new_data['articles']
        for i in self.artical:
            self.result.append(i['title'])
        self.VA.speak(" here are to top news from techcrunch ")
        for i in range(5):
            print(i+1,self.result[i])
            self.VA.speak(str(self.result[i]))


if __name__ == '__main__':
    test=weatherandNews()
    print(test.news("corona"))