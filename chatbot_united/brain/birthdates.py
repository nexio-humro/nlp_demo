from brain.filters import query_filter
import datefinder
import wikipedia
wikipedia.set_lang("pl")


def birthdate_finder(query):
    datelist = []
    try:
        search = wikipedia.search(query, results=3)
        for i in range(len(search)):
            user_answer = input(f'{search[i]}, tak? [tak/nie]').lower()
            if user_answer == 'tak':            
                article_summary = wikipedia.summary(search[i], sentences=6)
                date_matches = datefinder.find_dates(article_summary)
                for match in date_matches:
                    datelist.append(match)
                birthdate = datelist[1].strftime('%Y')
                return int(birthdate), article_summary
        print("Poddaję się, zadaj proszę inne pytanie")
    except:
        print("Niestety nie rozumiem, spróbuj proszę zapytać proszę o coś innego.")


def wikipedia_age_search(query):
    try:
        query_filtered = query_filter(query)
        birthdate, article = birthdate_finder(query_filtered)
        age = 2022 - birthdate
        print(is_alive(age, article))
    except:
        pass


def is_alive(age, article):
    if article.find('zm.') == -1:
        return 'Rocznikowo ' + str(age) 
    else:
        return "Przykro mi, ale z tego co mi wiadomo ta osoba już nie żyje."