import wikipedia
from brain.filters import nested_dot_filter, query_filter


def wikipedia_search(query):
    query_filtered = query_filter(query)
    articles = wikipedia.search(query_filtered, results=3)
    try:
        for i in range(len(articles)):
            user_answer = input(f'{articles[i]}, tak? [tak/nie]').lower()
            if user_answer == 'tak':            
                article_summary = wikipedia.summary(articles[i], sentences=6)
                article_filtered = nested_dot_filter(article_summary)
                article_filtered_splitted = article_filtered.split(".")
                if len(article_filtered_splitted)>=3:
                    print(article_filtered_splitted[0] + '.' 
                          + article_filtered_splitted[1] + '.' 
                          + article_filtered_splitted[2] + '.')
                    break
                else:
                    for s in range(len(article_filtered_splitted)):
                        print(article_filtered_splitted[s] + '.')
                        break
        if (i==2):
            print("Poddaję się, zadaj proszę inne pytanie")
    except Exception as E:
        print(E)
        print("Poddaję się, zadaj proszę inne pytanie")
