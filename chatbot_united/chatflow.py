from chatbot_api import Chatbot

from text_preprocessor import TextPreprocessor
from brain.math import do_math
from brain.birthdates import wikipedia_age_search, birthdate_finder
from brain.filters import commas_to_dots
from brain.time import get_time, get_weekday
from brain.wikipedia_search import wikipedia_search
from brain.voice import text_to_speech
from brain.voice import speech_to_text
from brain.currency import get_rate_x_to_pln
from brain.temperature import show_temperature


smalltalk_counter = 0


class Chatflow:
    def __init__(self):
        pass

    def human_detection(self):
        return True


    def id_verifiction(self):
        return 'Ok, muszę zweryfikować Twoją tożsamość. Pokaż proszę dowód osobisty do kamery.'
    
    def welcome(self):
        return 'Cześć! Miło Cię widzieć. W czym moge pomóc?'

    def flow(self, voice=False, buisness_hint=False):
        global smalltalk_counter
        if self.human_detection():
            if voice==True:
                text_to_speech(self.welcome())
            print(self.welcome())
        while self.human_detection():
            print(smalltalk_counter)
            stop_conversation = chatbot_test.ask(voice=voice)
            if stop_conversation == True:
                break
            if buisness_hint == True:
                if smalltalk_counter > 2:
                    if voice==True:
                        text_to_speech('Fajnie się gawędzi, ale pozwól że przedstawię Ci ofertę')
                    print('Fajnie się gawędzi, ale pozwól że przedstawię Ci ofertę')
                    chatbot_test.show_offer()
                    # global smalltalk_counter
                    # user_input = str(speech_to_text())
                    if voice==True:
                        user_input = speech_to_text(duration=11, bar_status=False)
                    else:
                        user_input = input("You:")
                    if user_input != 0:
                        if user_input.find('jeden') !=-1 or user_input.find('dwa') !=-1 or user_input.find('trzy') !=-1 or user_input.find('cztery') !=-1 or user_input.find('1') !=-1 or user_input.find('2') !=-1 or user_input.find('3') !=-1 or user_input.find('4') !=-1:
                            verification = self.id_verifiction()
                            print(verification)
                            if voice==True:
                                text_to_speech(verification)
                            print('Awaiting for vision module response...')
                        elif user_input.find('pięć') !=-1 or user_input.find('5') != -1:
                            print('Ok, obsługa zaraz podejdzie')
                            text_to_speech('Ok, obsługa zaraz podejdzie')
                        else:
                            pass
                    smalltalk_counter = 0



if __name__ == "__main__":     
    chatbot_test = Chatbot()
    chatflow = Chatflow()
    chatflow.flow(voice=True, buisness_hint=False)

# chatbot = Chatbot()
# # chatbot.chat(voice=False)