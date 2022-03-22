from matplotlib.pyplot import text
from brain.filters import query_filter
import datefinder
import wikipedia
from brain.voice import speech_to_text, text_to_speech
wikipedia.set_lang("pl")


def birthdate_finder(query, voice):
    datelist = []
    try:
        search = wikipedia.search(query, results=3)
        for i in range(len(search)):
            print(f'{search[i]}, tak?')
            if voice==True:
                text_to_speech(f'{search[i]}, tak?')
                user_answer = str(speech_to_text())
            else:
                user_answer = input("You:")
            if user_answer.lower().find('nie') == -1:            
                article_summary = wikipedia.summary(search[i], sentences=6)
                date_matches = datefinder.find_dates(article_summary)
                for match in date_matches:
                    datelist.append(match)
                birthdate = datelist[1].strftime('%Y')
                return int(birthdate), article_summary
        print("Poddaję się, zadaj proszę inne pytanie")
        if voice==True:
            text_to_speech("Poddaję się, zadaj proszę inne pytanie")
    except:
        print("Niestety nie rozumiem, spróbuj proszę zapytać proszę o coś innego.")
        if voice==True:
            text_to_speech("Niestety nie rozumiem, spróbuj proszę zapytać proszę o coś innego.")


def wikipedia_age_search(query, voice):
    try:
        query_filtered = query_filter(query)
        birthdate, article = birthdate_finder(query_filtered, voice)
        age = 2022 - birthdate
        # print(is_alive(age, article))
        return is_alive(age, article)
        # text_to_speech(is_alive(age, article))
    except:
        pass


def is_alive(age, article):
    if article.find('zm.') == -1:
        return "Rocznikowo " + str(age) 
    else:
        return "Przykro mi, ale z tego co mi wiadomo ta osoba już nie żyje."