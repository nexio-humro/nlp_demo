## https://techwithtim.net/tutorials/ai-chatbot/part-1/#google_vignette

import json
import os
import pickle

import matplotlib.pyplot as plt
import nltk
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow import keras

# %%
from text_preprocessor import TextPreprocessor

text_preprocessor = TextPreprocessor()
current_dir = os.path.dirname(os.path.abspath(__file__))

#%%
with open(current_dir + '/data/data.json', encoding='utf8') as file:
    data = json.load(file)

#%%
words = []
labels = []
docs_x = []
docs_y = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        lemmatized_sentence: str = text_preprocessor.lemmatize(pattern)
        if lemmatized_sentence != '':
            tokenized_words = nltk.word_tokenize(lemmatized_sentence)
            words.extend(tokenized_words)
            docs_x.append(tokenized_words)
            docs_y.append(intent["tag"])
        if intent["tag"] not in labels:
            labels.append(intent["tag"])
words = [w.lower() for w in words if w != "?"]
words = sorted(list(set(words)))
labels = sorted(labels)
features = []
output = []

out_empty = np.zeros(len(labels), dtype=int)

for x, doc in enumerate(docs_x):
    bag = []
    tokenized_words = [w.lower() for w in doc]

    for w in words:
        if w in tokenized_words:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    features.append(bag)
    output.append(output_row)

#%%
# training = np.array(features)
# output = np.array(output)

# print(training[0])
# print(training.shape)
#%%

KFolds = 10
histories = []
for i in range(KFolds):
    X_train, X_test, y_train, y_test = train_test_split(features, output, test_size=0.33, stratify=output)

    with open(current_dir + '/data/data.pickle', "wb") as f:
        pickle.dump((words, labels, features, output), f)

        tf.compat.v1.reset_default_graph()
        keras.backend.clear_session()
        layers = keras.layers


        model = keras.Sequential(
            [
                layers.Dense(128, input_shape=(None, len(words)), activation='relu'),
                layers.Dropout(0.2),
                layers.Dense(64, activation='relu'),
                layers.Dropout(0.2),
                layers.Dense(len(output[0]), activation='sigmoid')
            ]
        )

        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

        history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=225, batch_size=8)
        histories.append(history)

        model.save(current_dir + '/models/model')

#%%

acc = 0
val_acc = 0
for history in histories:
    acc += history.history['accuracy'][-1] / len(histories)
    print(history.history['val_accuracy'][-1])
    val_acc += history.history['val_accuracy'][-1] / len(histories)

#%%
plt.plot(history.history['accuracy'], 'r', history.history['val_accuracy'], 'b')
plt.show()

print(acc)
print(val_acc)