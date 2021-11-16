from ecapture import ecapture as ec
import time 
import subprocess
import winshell
from voice_assi import Assistant


class Wincmd():
    def __init__(self):
        self.VA=Assistant()
        self.setting = self.VA.settings

    def camera(self):
        self.VA.speak("smile................")
        ec.capture(0, "Jarvis Camera ", "img.jpg")

    def log_out(self):
        self.VA.speak("Make sure all the application are closed before sign-out")
        time.sleep(5)
        subprocess.call(["shutdown", "/l"])

    def restr(self):
        subprocess.call(["shutdown", "/r"])
    
    def empyrec(self):
        winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
        self.VA.speak("Recycle Bin Recycled")
    # opeb cmd prompt   

    def cmd(self):
        subprocess.call(["cmd"])            
    # open notepad in windows
    def notepad(self):
        subprocess.call(["notepad"])
        
        

