# porównanie kilku modeli klasyfikacji - najlepiej sprawdził się SVM
# https://towardsdatascience.com/multi-class-text-classification-with-scikit-learn-12f1e60e0a9f -

# stop words
# https://pl.wikipedia.org/wiki/Wikipedia:Stopwords
# https://github.com/bieli/stopwords/blob/master/polish.stopwords.txt

# %%
# Imports
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
from sklearn.calibration import CalibratedClassifierCV
import joblib
import pickle
import json
from text_preprocessor import TextPreprocessor

text_preprocessor = TextPreprocessor()

# %%
class ColumnNames:
    Text = 'text'
    Category = 'category'


df: pd.DataFrame = pd.read_csv("data/klasyfikacjacsv.csv", encoding='windows-1250',
                               names=[ColumnNames.Text, ColumnNames.Category])

df = df[df[ColumnNames.Category] != 0]

# %%
df[ColumnNames.Text] = df[ColumnNames.Text].apply(lambda sentence: text_preprocessor.lemmatize(sentence))

# %%
with open("chatbot/data/data.json", encoding='utf8') as file:
    data = json.load(file)

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        df2 = pd.DataFrame({ColumnNames.Text: [pattern],
                            ColumnNames.Category: [3]})
        df = df.append(df2, ignore_index=True)

# %%
tfidf = TfidfVectorizer(sublinear_tf=True, ngram_range=(1, 2), norm='l2', stop_words=text_preprocessor.all_stopwords)
features: np.ndarray = tfidf.fit_transform(df[ColumnNames.Text])
labels = df[ColumnNames.Category]

print(len(tfidf.vocabulary_))
with open("models/tfidf.pkl", 'wb') as handle:
    pickle.dump(tfidf, handle)

svm = SVC(kernel='linear')
clf = CalibratedClassifierCV(svm)

X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(features, labels, df.index,
                                                                                 stratify=labels,
                                                                                 test_size=0.2, random_state=0)

clf.fit(X_train, y_train)

# %%
joblib.dump(clf, 'models/model.pkl')
