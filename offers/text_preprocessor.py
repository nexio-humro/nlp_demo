# %%
import spacy
from singleton import SingletonMeta as __SingletonMeta


class TextPreprocessor(metaclass=__SingletonMeta):
    __nlp: spacy

    def __init__(self):
        self.__nlp = spacy.load("pl_core_news_md")
        self.all_stopwords = self.__nlp.Defaults.stop_words

    def lemmatize(self, sentence: str) -> str:
        return ' '.join([w.lemma_ for w in self.__nlp(sentence) if w not in self.all_stopwords])
