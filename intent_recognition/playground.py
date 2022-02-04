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
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.metrics import f1_score
import numpy as np
from sklearn.model_selection import LeaveOneOut
from sklearn.calibration import CalibratedClassifierCV
import joblib
import pickle
from text_preprocessor import TextPreprocessor

# %%
# Load data
text_preprocessor = TextPreprocessor()

class ColumnNames:
    Text = 'text'
    Category = 'category'


df: pd.DataFrame = pd.read_csv("./data/klasyfikacjacsv.csv", encoding='windows-1250',
                               names=[ColumnNames.Text, ColumnNames.Category])

print(df.shape)
df = df[df[ColumnNames.Category] != 0]
print(df.shape)

# %%

plt.hist(df[ColumnNames.Category])
plt.show()

#%%
df[ColumnNames.Text] = df[ColumnNames.Text].apply(lambda sentence: text_preprocessor.lemmatize(sentence))

# %%
tfidf = TfidfVectorizer(sublinear_tf=True, ngram_range=(1, 2), norm='l2', stop_words=text_preprocessor.all_stopwords)
features: np.ndarray = tfidf.fit_transform(df[ColumnNames.Text])
labels = df[ColumnNames.Category]
features.shape

with open("./models/tfidf.pkl", 'wb') as handle:
    pickle.dump(tfidf, handle)

# %%

plt.hist(labels)
plt.show()

# %%
svm = SVC(kernel='linear')
clf = CalibratedClassifierCV(svm)

# stratify=labels,
X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(features, labels, df.index,
                                                                                 stratify=labels,
                                                                                 test_size=0.2, random_state=0)
# plt.hist(y_train)
# plt.hist(y_test)
# plt.show()

clf.fit(X_train, y_train)
y_proba = clf.predict_proba(X_test)
y_pred = clf.predict(X_test)
print(y_pred)

conf_mat = confusion_matrix(y_test, y_pred)
print(conf_mat)
print(f1_score(y_test, y_pred, average='macro'))

# %%
joblib.dump(clf, './models/model.pkl')

# %%
# Outliers
# isf = IsolationForest(n_jobs=-1, random_state=1)
# isf.fit(X_train, y_train)
#
# print(isf.score_samples(X_train).min())
# np.where(X_train == isf.score_samples(X_train).min())
# %%

fig, ax = plt.subplots(figsize=(10, 10))
sns.heatmap(conf_mat, annot=True, fmt='d')
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()

# %%
# Cross Validation

clf = SVC(kernel='linear')
# clf = LogisticRegression(penalty='l2', C=1)

scores: np.ndarray = cross_val_score(clf, features, labels, cv=LeaveOneOut(), scoring='f1_macro')
# scores: np.ndarray = cross_val_score(clf, features, labels, cv=20, scoring='f1_macro')
print(f"Średni wynik: {scores.mean()}")

# np.where(scores == 0)

# %%
svm = SVC(kernel='linear')
clf = CalibratedClassifierCV(svm)
clf.fit(X_train, y_train)

sentence = "Chcę kupić numer"
lematized_sentence: str = ''

for word in sentence.split(' '):
    lematized_sentence += text_preprocessor.lemmatize(word) + ' '

# test = tfidf.transform([lematize("Chcę") + " " + lematize("Zgłosić") + " " + lematize("reklamację")])
test = tfidf.transform([lematized_sentence])
print(clf.predict(test))
print(clf.predict_proba(test))
