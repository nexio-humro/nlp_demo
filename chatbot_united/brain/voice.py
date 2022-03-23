from sys import breakpointhook
import speech_recognition as sr
import pyttsx3 as tts
from matplotlib.pyplot import text



engine = tts.init()
engine.setProperty('rate', 130)
engine.setProperty('voice', 'polish')

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    # depends on microphone type/noise etc
    recognizer.energy_threshold = 200
    with sr.Microphone() as source:
        try:
            print("nasłuchuję...")
            # audio = recognizer.listen(source, timeout=3.5)
            audio = recognizer.record(source, duration=3.5)
            # print("rozpoznaję...")
            text = recognizer.recognize_google(audio, language='pl-PL')
            if text != '':
                print(text)
                return text
            return 0
        except:
            return 0


def record():
    with sr.Microphone() as source:
        try:
            print("nasłuchuję...")
            audio = recognizer.record(source, duration=3.5)
            # print(audio)
            # print(type(audio))
            text = recognizer.recognize_google(audio, language='pl-PL')
            print(text)
            if text != '':
                print(text)
                return text
            return 0
        except:
            return 0

# mow('cześć jestem robotem firmy neksjo bardzo mi miło')
# while True:
#     txt = speech_to_text()
#     if not txt == 0:
#         print(txt)
#         text_to_speech(txt)
#         break
#     else:
#         print('nie udalo sie ropoznac')
#         continue