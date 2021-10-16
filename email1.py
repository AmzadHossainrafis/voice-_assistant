import csv 
import smtplib
from voice_assi import Assistant
from twilio.rest import Client

class MailandCont():
    def __init__(self,name):
        self.name = name
        self.VA= Assistant()
        self.setting= self.VA.settings
        self.email=self.setting.user_email
        self.user_password=self.setting.user_pass
        self.sid=self.setting.Sid
        self.ath=self.setting.ath
        self.Tnumber=self.setting.Tnumber

        
        
        
    
    def find(self):
        self.filename=self.setting.csv_dir
        with open(self.filename,'r',encoding="utf8") as f:
            reader = csv.reader(f)


            for row in reader:

                if row[1].lower()== self.name.lower():
                
                    user_name = row[1]
                    user_email = row[0]
                    user_phone = row[3]
                    #print(f"user name {user_name} user email {user_email} user_phone{user_phone}")


                    return {"user_name": str(user_name).lower(), 
                        "user_email": str(user_email).lower(),
                        "user_phone": f"+880{user_phone}",
                        }




#this fucntion take name as arg 
    def sendmail(self,msg):


        reciver=self.find()
        m=reciver["user_email"]
        server=smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.starttls()
        server.login(self.email,self.user_password)
        server.sendmail(self.email,str(m),str(msg))
        print(f" mail is send to{m} ")
        server.quit()



    def sendsms(self):
        """problem : having prb to recieve the msg but msg are properly send """
        reciver=self.find()
        test_msg="this is a test masg "
        m=reciver["user_phone"]
        client=Client(self.sid,self.ath)
        message=client.messages.create(to="+8801913091194",from_=self.Tnumber,body=test_msg)
        print(message.sid)
        
if __name__ == '__main__':
    test=MailandCont("Mobasshir")
    test.sendmail()