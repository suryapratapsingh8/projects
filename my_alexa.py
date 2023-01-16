import datetime
import speech_recognition as sp
import pyttsx3
import pywhatkit
import pywhatkit as kt
import pyjokes
listner =sp.Recognizer()
engine=pyttsx3.init() 

engine.say(' hello sir! I am surya . how can i help you ') 
engine.runAndWait()
def talk(text):
   engine.say(text) 
   engine.runAndWait()
def xyz():
    print('you should start speaking with word surya:')
    talk('you should start speaking with word surya:')
    result()
def abc():
    quit()
   
def result():
    try:
        with sp.Microphone() as source:
            print('listening....')
            voice = listner.listen(source)
            cmd = listner.recognize_google(voice)
            cmd=cmd.lower()
            if 'surya' in cmd:
                cmd=cmd.replace('surya', '')
                print(cmd)
            elif 'surya' not in cmd:
                xyz()
            
            
    except:
        xyz()
    return cmd
def run_surya():
    command = result()
    print(command)
    if 'play' in command:
        song=command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time= datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is'+ time )
    elif 'search' in command:
        result1=command.replace('search' , '')
        talk('searching' + result1)
        kt.search(result1)
    elif 'single' in command:
        
        talk('No, I am in relationship with coding')
    elif 'close' in command:
        result()
    elif 'how are you' in command:
        talk('I am fine.')
    elif 'how is your day' in command:
        talk('It was a busy day full of enjoyment')
    elif 'good bye' in command:
        talk('bye bye sir')
        abc()
    elif '' in command:
        talk('Bol Bhosdike')

    
    elif 'jokes' in command:
        talk(pyjokes.get_joke())
    else:
        talk("please say the command again")
        
while True:    
  run_surya()
