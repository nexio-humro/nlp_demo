import speech_recognition as sr
from matplotlib.pyplot import text
import pyaudio
from gtts import gTTS
import os
import playsound
import time
from tqdm import tqdm
import threading

def progress_bar():
    time.sleep(0.3)
    for i in tqdm(range(25)):
        time.sleep(0.1)


def text_to_speech(text):
    tts = gTTS(text, lang='pl')
    tts.save('expression.mp3')
    playsound.playsound('expression.mp3')
    os.remove('expression.mp3')


def speech_to_text_ruchome():
    recognizer = sr.Recognizer()
    # depends on microphone type/noise etc
    with sr.Microphone(device_index=0) as source:
        try:
            # audio = recognizer.listen(source, timeout=3.5)
            recognizer.adjust_for_ambient_noise(source, duration=0.8)
            # recognizer.dynamic_energy_threshold = True 
            print("nasłuchuję...")
            # audio = recognizer.listen(source)
            audio = recognizer.listen(source,timeout=8,phrase_time_limit=8)
            # print("rozpoznaję...")
            text = recognizer.recognize_google(audio, language='pl-PL')
            if text != '':
                print(text)
                return text
            return 0
        except:
            return 0


def speech_to_text():
    recognizer = sr.Recognizer()
    # depends on microphone type/noise etc
    # recognizer.energy_threshold = 350
    with sr.Microphone() as source:
        try:
            # audio = recognizer.listen(source, timeout=3.5)
            progress_bar_thread = threading.Thread(target=progress_bar, name="progress_bar")
            progress_bar_thread.start()
            print("nasłuchuję...")
            audio = recognizer.record(source, duration=3.5)
            
            # print("rozpoznaję...")
            text = recognizer.recognize_google(audio, language='pl-PL')
            if text != '':
                print(text)
                return text
            return 0
        except:
            return 0


#STARE FUNKCJE

def record():
    recognizer = sr.Recognizer()
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

def wav_to_text(filename):
    r = sr.Recognizer()
    jackhammer = sr.AudioFile(filename)
    with jackhammer as source:
        try:
            audio = r.record(source)
            text = r.recognize_google(audio, language='pl-PL')
            print(text)
            if text != '':
                print(text)
                return text
            return 0
        except:
            return 0


def voice_to_wav():
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 4.5
    filename = "PYAUDIO.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()




def speech_to_textXXXX():
    voice_to_wav()
    wav_to_text(r'C:\Users\lenovo\Desktop\nlp_demo\chatbot_united\PYAUDIO.wav')

#wav_to_text(r'C:\Users\lenovo\Desktop\nlp_demo\chatbot_united\brain\voice_rec.wav')
# wav_to_text(r'C:\Users\lenovo\Desktop\nlp_demo\PYAUDIO.wav')
#speech_to_text_ALTERNATIVE()

# import sounddevice as sd
# import pyttsx3
# engine = pyttsx3.init()
# def text_to_speech_LOW_QUALITY(text):
#     engine.setProperty('rate', 130)
#     engine.setProperty('voice', 'polish')
#     engine.say(text)
#     engine.runAndWait()