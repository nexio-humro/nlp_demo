import json
import os
import pickle
import random

import nltk
import numpy as np
from tensorflow import keras

# from offers.text_preprocessor import TextPreprocessor
from text_preprocessor import TextPreprocessor
from brain.math import do_math
from brain.birthdates import wikipedia_age_search, birthdate_finder
from brain.which_time import which_time
from brain.wikipedia_search import wikipedia_search


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
        with open(current_dir + '\data\data.json', encoding='utf8') as file:
            self.__data = json.load(file)

        with open(current_dir + '\data\data.pickle', 'rb') as f:
            self.__words, self.__labels, self.__training, self.__output = pickle.load(f)

        self.__model = keras.models.load_model(current_dir + '/models/model/chatbot.keras')
        for intent in self.__data["intents"]:
            for pattern in intent["patterns"]:
                    tokenized_pattern = nltk.word_tokenize(pattern.lower())
                    words.extend(tokenized_pattern)

        words = [self.__text_preprocessor.lemmatize(w) for w in words]
        words = sorted(list(set(words)))

    # %%

    def bag_of_words(self, sentence, words):
        bag = [0 for _ in range(len(words))]
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [self.__text_preprocessor.lemmatize(word.lower()) for word in sentence_words]

        for s in sentence_words:
            for i, w in enumerate(words):
                if w == s:
                    bag[i] = 1
        return np.array(bag)

    # %%
    def question(self, cause_text: str):
        bag =  self.bag_of_words(sentence=cause_text, words=self.__words)
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


    def chat(self):
        print("Cześć! W czym Ci mogę pomóc? [napisz 'koniec' aby zakończyć rozmowę]")
        while True:
            user_input = input("You:")
            if user_input.lower() == "koniec":
                break
            results1 = self.bag_of_words(user_input, words=self.__words)
            results1 = np.array([results1])
            predictions = self.__model.predict(results1)
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
                        if tag == 'wikipedia':
                            responses = t['responses']
                            print(random.choice(responses))
                            wikipedia_search(query=user_input.lower())
                        elif tag == 'google':
                            responses = t['responses']
                            print(random.choice(responses))
                            print('under construction')
                            # google(query=user_input.lower())
                        elif tag == 'wikipedia-age':
                            responses = t['responses']
                            print(random.choice(responses))
                            wikipedia_age_search(query=user_input.lower())
                        elif tag == 'smalltalk-math':
                            responses = t['responses']
                            print(random.choice(responses))
                            do_math(query=user_input.lower())
                        elif tag == 'smalltalk-time':
                            responses = t['responses']
                            print(random.choice(responses))
                            which_time()
                        elif tag == 'smalltalk-weather':
                            responses = t['responses']
                            print(random.choice(responses))
                            print('under construction')
                            # show_temperature()
                        else:
                            responses = t['responses']
                            print(random.choice(responses))
            else:
                print("Nie zrozumiałem, proszę zadaj inne pytanie")

if __name__ == "__main__":
    chatbot = Chatbot()

    chatbot.chat()