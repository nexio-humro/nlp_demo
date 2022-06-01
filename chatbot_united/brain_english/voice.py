import speech_recognition as sr
from matplotlib.pyplot import text
import pyaudio
from gtts import gTTS
import os
import playsound
import time
from tqdm import tqdm
import threading
import pyttsx3


def progress_bar():
    time.sleep(0.3)
    for i in tqdm(range(25)):
        time.sleep(0.1)


def text_to_speech(text):
    tts = gTTS(text, lang='en')
    tts.save('expression.mp3')
    playsound.playsound('expression.mp3')
    os.remove('expression.mp3')


def speech_to_text_ruchome():
    recognizer = sr.Recognizer()
    # depends on microphone type/noise etc
    with sr.Microphone(device_index=0) as source:
        try:
            # audio = recognizer.listen(source, timeout=3.5)
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            # recognizer.dynamic_energy_threshold = True 
            print("listening...")
            # audio = recognizer.listen(source)
            # audio = recognizer.listen(source,timeout=8,phrase_time_limit=8)
            audio = recognizer.listen(source)
            # print("rozpoznaję...")
            text = recognizer.recognize_google(audio, language='en-EN')
            if text != '':
                print(text)
                return text
            return 0
        except:
            return 0


def speech_to_text(duration=3.5, bar_status=True):
    recognizer = sr.Recognizer()
    # depends on microphone type/noise etc
    # recognizer.energy_threshold = 350
    with sr.Microphone() as source:
        try:
            # audio = recognizer.listen(source, timeout=3.5)
            if bar_status == True:
                progress_bar_thread = threading.Thread(target=progress_bar, name="progress_bar")
                progress_bar_thread.start()
            print("listening...")
            audio = recognizer.record(source, duration=duration)
            
            # print("rozpoznaję...")
            text = recognizer.recognize_google(audio, language='en-US')
            if text != '':
                print(text)
                return text
            return 0
        except:
            return 0

# text_to_speech_english('hey how are you doing')