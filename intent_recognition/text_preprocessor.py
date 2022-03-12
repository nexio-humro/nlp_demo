# %%
import spacy
from intent_recognition.singleton import SingletonMeta as __SingletonMeta


class TextPreprocessor(metaclass=__SingletonMeta):
    __nlp: spacy

    def __init__(self):
        self.__nlp = spacy.load("pl_core_news_md")
        self.all_stopwords = self.__nlp.Defaults.stop_words

    def lemmatize(self, sentence: str) -> str:
        lematized_sentence: str = ''
        for w in self.__nlp(sentence):
            if not w.text.lower() in self.all_stopwords:
                lematized_sentence += w.lemma_ + ' '
        return lematized_sentence

lemanter = TextPreprocessor()

print(lemanter.lemmatize("paryżu"))