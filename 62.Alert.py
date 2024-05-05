import time
from win32com.client import Dispatch
from win10toast import ToastNotifier

REPEAT_INTERVAL=10#rrepeat frequency in seconds

def notify_and_speak(message):
    #display a toast notification
    toaster=ToastNotifier()
    toaster.show_toast('water remainder',message,duration=5)#hide the main window
    
    #speak the message
    speaker=Dispatch('SAPI.SpVoice')
    speaker.Speak(message)
    
while True:
    notify_and_speak('hey harry,drink water')
    time.sleep(REPEAT_INTERVAL)