import time
import pyttsx3


def countdown(t):

  while t:

    mins, secs = divmod(t, 60)

    timer = '{:02d}:{:02d}'.format( mins, secs)

    print(timer, end="\r")

    time.sleep(1)

    t -= 1

print('countdown timer is ready!')


t = input("Enter the time in seconds: ")



countdown(int(t))
engine=pyttsx3.init() 

engine.say("Study Motherfucker\n"*3)   
engine.runAndWait()

