import pyautogui as pt 
import time
import pywhatkit


#phone no , message, time (24hrs) , boolean , closing time

times=int(input('Enter number of times you want to send the message: '))

message=input('Enter the message: ')
time.sleep(3)


i=0

while i<int(times):
    print(message)
    
    i=i+1
    
p=pywhatkit.sendwhatmsg('+919695231025', message, 11,26,15,True,3)