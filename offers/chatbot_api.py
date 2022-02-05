import json
import os
import pickle
import random

import nltk
import numpy as np
from tensorflow import keras

from text_preprocessor import TextPreprocessor


class Chatbot:
    __text_preprocessor: TextPreprocessor
    __tag_history = []
    __data = None
    __model = None
    
    def __init__(self, threshold=0.55):
        self.threshold = threshold

        words = []
        print("chatbot-offers init")
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
        print("Nexiobot na Ciebie czeka! [napisz 'koniec' aby zakończyć rozmowę]")
        while True:
            user_input = input("You:")
            if user_input.lower() == "koniec":
                break
            
            bag =  self.bag_of_words(sentence=user_input, words=self.__words)

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


chatbot: Chatbot = Chatbot()

# chatbot.question("siema przedstaw się")
chatbot.chat()