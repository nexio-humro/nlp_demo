import joblib
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import List, Dict
from sklearn.calibration import CalibratedClassifierCV
from intent_recognition.text_preprocessor import TextPreprocessor
import os

# %%
class IntentClassification:
    __tfidf: TfidfVectorizer
    __clf: CalibratedClassifierCV

    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.text_preprocessor = TextPreprocessor()
        self.__tfidf = pickle.load(open(current_dir + "/models/tfidf.pkl", "rb"))
        self.__clf = joblib.load(current_dir + '/models/model.pkl')

    def __categoriesFromClass(self):
        categories_dict: Dict = {}

        for (key, value) in IntentClassification.Categories.__dict__.items():
            if not key.startswith("__"):
                categories_dict[key] = value

        categories_values: List[int] = []
        for category in categories_dict:
            categories_values.append(categories_dict[category])
        return categories_values

    class Categories:
        BuyingNumber = 1
        Complaint = 2
        Question = 3

    def predict(self, sentence: str) -> int:
        lematized_sentence: str = self.text_preprocessor.lemmatize(sentence)

        transformed_sentence = self.__tfidf.transform([lematized_sentence])
        return self.__clf.predict(transformed_sentence)[0]
