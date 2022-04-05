import speech_recognition as sr
import pyttsx3 as pyx3
from pyaudio import PyAudio
# Initialize the speech recognizer

pyaud = PyAudio()
recognizer = sr.Recognizer()
engine = pyx3.init()
engine.setProperty('volume', '0.7')
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
# Function to convert Text 2 Speech
def SpeakText(command):
    

    if(command=='hey'):
        engine.say('Sup bitch.')
    if(command=='how are you doing'):
        engine.say('Fuck off cunt.')
        engine.say('Im doing alright')
    if(command=='list voices'):
        engine.say('Here are the list of voices')
        printVoices()
    engine.runAndWait()

def printVoices():
    voices = engine.getProperty('voices')

    for voice in voices:
        print("##Voice {}##".format(voice.name))
        print("ID: {}".format(voice.id))
        print("Name: {}".format(voice.name))
        print("Age: {}".format(voice.age))
        print("Gender: {}".format(voice.gender))
        print("Languages known: {}".format(voice.languages))
        engine.say(voice.name)

while(1):
    try:
        with sr.Microphone() as source2:
            recognizer.adjust_for_ambient_noise(source2, duration=1)
            print("Listening...")
            audio2 = recognizer.listen(source2)
            
            print("Processing input...")
            MyText = recognizer.recognize_google(audio2)

            print("Did you say: ", MyText)
            SpeakText(MyText.lower())

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occured")
