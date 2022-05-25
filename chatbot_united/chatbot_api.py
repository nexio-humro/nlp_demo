import json
import os
import pickle
import random

from matplotlib.pyplot import text
import nltk
import numpy as np
from tensorflow import keras
# from offers.text_preprocessor import TextPreprocessor
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

class Chatbot:
    __text_preprocessor: TextPreprocessor
    __tag_history = []
    __data = None
    __model = None
    
    def __init__(self, threshold=0.55):
        self.threshold = threshold
        words = []
        print("chatbot-united init")
        self.__text_preprocessor = TextPreprocessor()
        # %%
        current_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(current_dir,'data', 'data.json'), encoding='utf8') as file:
            self.__data = json.load(file)

        with open(os.path.join(current_dir ,'data', 'data.pickle'), 'rb') as f:
            self.__words, self.__labels, self.__training, self.__output = pickle.load(f)

        self.__model = keras.models.load_model(current_dir + '/models/model/united_model')
        for intent in self.__data["intents"]:
            for pattern in intent["patterns"]:
                    tokenized_pattern = nltk.word_tokenize(pattern.lower())
                    words.extend(tokenized_pattern)

        words = [self.__text_preprocessor.lemmatize(w) for w in words]
        words = sorted(list(set(words)))

    # %%

    def bag_of_words(self, sentence, all_words):
        bag = [0 for _ in range(len(all_words))]
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [self.__text_preprocessor.lemmatize(word.lower()) for word in sentence_words]

        for s in sentence_words:
            for i, w in enumerate(all_words):
                if w == s:
                    bag[i] = 1
        return np.array(bag)

    # %%
    def question(self, cause_text: str):
        bag =  self.bag_of_words(sentence=cause_text, all_words=self.__words)
        results = self.__model.predict(np.array([bag]))
        results_index = np.argmax(results)
        tag = self.__labels[results_index]
        
        if results[0][results_index] > self.threshold:
            for t in self.__data["intents"]:
                if t['tag'] == tag:
                    responses = t['responses']
                    print(random.choice(responses))
        else:
            print("Nie zrozumiałem, proszę zadaj inne pytanie.")


    def chat(self, voice=False):
        print("Cześć! W czym Ci mogę pomóc? [napisz 'koniec' aby zakończyć rozmowę]")
        if voice==True:
            text_to_speech("Cześć! W czym Ci mogę pomóc? [aby zakończyć rozmowę powiedz 'koniec']")
        while True:
            if voice==True:
                user_input = str(speech_to_text())
            else:
                user_input = input("You:")
            if user_input != '0':
                if user_input.lower() == "koniec":
                    break
                common_words = self.bag_of_words(user_input, all_words=self.__words)
                common_words = np.array([common_words])
                predictions = self.__model.predict(common_words)
                results_index = np.argmax(predictions)
                tag = self.__labels[results_index]
                if user_input.find('--confidence') != -1:
                    print('confidence:', predictions[0][results_index])
                if user_input.find('--tag') != -1:
                    print('tag:', tag)
                if predictions[0][results_index] > self.threshold:
                    for t in self.__data["intents"]:
                        if t['tag'] == tag:
        #                     print(tag)
                            if tag == 'smalltalk-wikipedia':
                                responses = t['responses']
                                print(random.choice(responses))
                                result = wikipedia_search(query=user_input.lower(), voice=voice)
                                print(result)
                                if voice==True:
                                    text_to_speech(result)
                                # if voice==True:
                                #     text_to_speech(wikipedia_search(query=user_input.lower(), voice=voice))
                                # else:
                                #     print(wikipedia_search(query=user_input.lower(), voice=voice))
                            elif tag == 'google':
                                responses = t['responses']
                                print(random.choice(responses))
                                print('under construction')
                                # google(query=user_input.lower())
                            elif tag == 'smalltalk-wikipedia-age':
                                responses = t['responses']
                                print(random.choice(responses))
                                result = wikipedia_age_search(query=user_input.lower(), voice=voice)
                                print(result)
                                if voice==True:
                                    text_to_speech(result)
                            elif tag == 'smalltalk-math':
                                responses = t['responses']
                                print(random.choice(responses))
                                result = do_math(query=user_input.lower())
                                if voice==True:
                                    text_to_speech(random.choice(responses))
                                    text_to_speech(str(result))
                                print(result)
                            elif tag == 'smalltalk-time':
                                responses = t['responses']
                                answer = random.choice(responses)
                                print(answer)
                                time = get_time()
                                print(time)
                                if voice==True:
                                    text_to_speech(answer)
                                    text_to_speech(time)
                            elif tag == 'smalltalk-weekday':
                                responses = t['responses']
                                answer = random.choice(responses)
                                print(answer)
                                print(get_weekday())
                                if voice==True:
                                    text_to_speech(get_weekday())
                            elif tag == 'smalltalk-weather':
                                responses = t['responses']
                                answer = random.choice(responses)
                                if voice==True:
                                    text_to_speech(answer)
                                print(answer)
                                temperature = show_temperature()
                                if voice==True:
                                    text_to_speech(temperature)
                                print(temperature)
                            
                            elif tag == 'smalltalk-currency':
                                responses = t['responses']
                                # print(random.choice(responses))
                                result = get_rate_x_to_pln(query=user_input.lower(), voice=voice)
                                if voice==True:
                                    text_to_speech(result)
                                print(result)
                                
                            else:
                                responses = t['responses']
                                answer = random.choice(responses)
                                print(answer)
                                if voice==True:
                                    answer = commas_to_dots(answer)
                                    text_to_speech(answer)
                else:
                    print("Nie zrozumiałem, proszę zadaj inne pytanie")
                    if voice==True:
                        text_to_speech("Nie zrozumiałem. proszę zadaj inne pytanie")


    def ask(self, voice=False):
        if voice==True:
            user_input = str(speech_to_text())
        else:
            user_input = input("You:")
        if user_input != '0':
            if user_input.lower() == "koniec":
                return True
            common_words = self.bag_of_words(user_input, all_words=self.__words)
            common_words = np.array([common_words])
            predictions = self.__model.predict(common_words)
            results_index = np.argmax(predictions)
            tag = self.__labels[results_index]
            if user_input.find('--confidence') != -1:
                print('confidence:', predictions[0][results_index])
            if user_input.find('--tag') != -1:
                print('tag:', tag)
            if predictions[0][results_index] > self.threshold:
                for t in self.__data["intents"]:
                    if t['tag'] == tag:
                        print(f"tag: {tag}")
                        if tag.find('smalltalk') != -1:
                            global smalltalk_counter
                            smalltalk_counter += 1
                        if tag == 'smalltalk-wikipedia':
                            responses = t['responses']
                            print(random.choice(responses))
                            result = wikipedia_search(query=user_input.lower(), voice=voice)
                            print(result)
                            if voice==True:
                                text_to_speech(result)
                        elif tag == 'smalltalk-google':
                            responses = t['responses']
                            print(random.choice(responses))
                            print('under construction')
                            # google(query=user_input.lower())
                        elif tag == 'smalltalk-wikipedia-age':
                            responses = t['responses']
                            print(random.choice(responses))
                            result = wikipedia_age_search(query=user_input.lower(), voice=voice)
                            print(result)
                            if voice==True:
                                text_to_speech(result)
                        elif tag == 'smalltalk-math':
                            responses = t['responses']
                            print(random.choice(responses))
                            result = do_math(query=user_input.lower())
                            if voice==True:
                                text_to_speech(random.choice(responses))
                                text_to_speech(str(result))
                            print(result)
                        elif tag == 'smalltalk-time':
                            responses = t['responses']
                            answer = random.choice(responses)
                            print(answer)
                            time = get_time()
                            print(time)
                            if voice==True:
                                text_to_speech(answer)
                                text_to_speech(time)
                        elif tag == 'smalltalk-weekday':
                            responses = t['responses']
                            answer = random.choice(responses)
                            print(answer)
                            print(get_weekday())
                            if voice==True:
                                text_to_speech(get_weekday())
                        elif tag == 'smalltalk-weather':
                            responses = t['responses']
                            answer = random.choice(responses)
                            if voice==True:
                                text_to_speech(answer)
                            print(answer)
                            temperature = show_temperature()
                            if voice==True:
                                text_to_speech(temperature)
                            print(temperature)
                        
                        elif tag == 'smalltalk-currency':
                            responses = t['responses']
                            # print(random.choice(responses))
                            result = get_rate_x_to_pln(query=user_input.lower(), voice=voice)
                            if voice==True:
                                text_to_speech(result)
                            print(result)
                            
                        else:
                            responses = t['responses']
                            answer = random.choice(responses)
                            print(answer)
                            if voice==True:
                                answer = commas_to_dots(answer)
                                text_to_speech(answer)
            else:
                smalltalk_counter += 1
                print("Nie zrozumiałem, proszę zadaj inne pytanie")
                if voice==True:
                    text_to_speech("Nie zrozumiałem.")


    def show_offer(self):
        print(
'''
=======================================
| 1. zmiana numeru                    |
| 2. zakup internetu                  |
| 3. informacie o moim koncie         |
| 4. rozwiązanie umowy                |
| 5. prośba o kontakt z człowiekiem   |
| brak wyboru -> powrót do smalltalk  |
=======================================
'''
    )




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