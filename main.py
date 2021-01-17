import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print (command)
    except:
        print ("Microphone not working correctly")
    return command

def run_jarvis():
    command = take_commad()
    print ("Command")
    if 'play' in command:
        song = command.replace('play', '')
        talk("Playing" + song)
        pywhatkit.playonyt("playing")

    elif 'time' in command:
        time = datetime.datetime.now().str('%H%M')
        print ("Time")
        talk("Current tme is" + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary (person)
        talk(info)
    elif 'date' in command:
        talk ("sorry, I have a headache")
    elif 'are you single' in command:
        talk ('I am in a relationship with WiFi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'siri' in command:
        talk("Who?")
    else:
        talk("Please say the command again")

while True:

    run_jarvis()
