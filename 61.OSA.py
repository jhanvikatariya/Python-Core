import time
import pyttsx3
from tkinter import Tk,messagebox

REPEAT_INTERVAL=10#rrepeat frequency in seconds

def notify_and_speak(message):
    #display a message box
    root=Tk()
    root.withdraw()#hide the main window
    messagebox.showinfo('water remainder',message)
    
    #speak the message
    engine=pyttsx3.init()
    engine.say(message)
    engine.runAndWait()
    
while True:
    notify_and_speak('hey jaladhi,drink water')
    time.sleep(REPEAT_INTERVAL)