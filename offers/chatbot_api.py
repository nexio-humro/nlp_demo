import json
import os
import pickle
import random

import nltk
import numpy as np
from tensorflow import keras

from offers.text_preprocessor import TextPreprocessor


class Chatbot:

    # nltk.download('punkt')
    __text_preprocessor: TextPreprocessor
    __tag_history = []
    __data = None
    __model = None

    def __init__(self):
        print("chatbot-offers init")
        self.__text_preprocessor = TextPreprocessor()
        # %%
        current_dir = os.path.dirname(os.path.abspath(__file__))
        with open(current_dir + '/data/data.json', encoding='utf8') as file:
            self.__data = json.load(file)

        with open(current_dir + '/data/data.pickle', 'rb') as f:
            self.__words, self.__labels, self.__training, self.__output = pickle.load(f)

        self.__model = keras.models.load_model(current_dir + '/models/model')

    # %%

    def bag_of_words(self, sentence: str):
        lematized_sentence: str = self.__text_preprocessor.lemmatize(sentence)
        s_words = nltk.word_tokenize(lematized_sentence)
        bag = np.array([1 if word in s_words else 0 for word in self.__words])
        return bag

    # %%
    def chat(self, cause_text: str):
            results = self.__model.predict(self.bag_of_words(cause_text))
            results_index = np.argmax(results)
            tag = self.__labels[results_index]

            responses = []
            for tg in self.__data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
                    break

            print(tag)
            print(responses[0:])
            return random.choice(responses)
chatbot: Chatbot = Chatbot()
chatbot.chat(cause_text="No siema mordo")