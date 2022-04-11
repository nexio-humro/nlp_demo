import numpy as np
import json
import nltk
import random
import pickle
import os
from text_preprocessor import TextPreprocessor

nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

lemmatizer = TextPreprocessor()
current_dir = os.path.dirname(os.path.abspath(__file__))

with open(current_dir + '/data/data.json', encoding='utf8') as file:
    data = json.load(file)

words = []
labels = []
docs_x = []
docs_y = []


for intent in data["intents"]:
    for pattern in intent["patterns"]:
            tokenized_pattern = nltk.word_tokenize(pattern.lower())
            words.extend(tokenized_pattern)
            docs_x.append(tokenized_pattern)
            docs_y.append(intent["tag"])
            
    if intent["tag"] not in labels:
        labels.append(intent["tag"])
        
words = [lemmatizer.lemmatize(w) for w in words]


words = sorted(list(set(words)))
labels = sorted(labels)

all_zipped = zip(docs_x,docs_y)
all = list(all_zipped)
random.shuffle(all)
docs_x, docs_y = zip(*all)
training = []
output = []
out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []
    lemmatized_pattern = [lemmatizer.lemmatize(w) for w in doc] 
    for w in words:
        if w in lemmatized_pattern:
            bag.append(1)
        else:
            bag.append(0)
            
    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1
    
    training.append(bag)
    output.append(output_row)

    with open(current_dir + '/data/data.pickle', "wb") as f:
        pickle.dump((words, labels, training, output), f)

