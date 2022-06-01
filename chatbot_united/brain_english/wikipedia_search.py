import wikipedia
from filters import nested_dot_filter, query_filter, cut_all_before_hyphen, shortcuts_filter, trim_details, trim_length
from voice import text_to_speech, speech_to_text
wikipedia.set_lang("en")


def wikipedia_search(query, voice):
    query_filtered = query_filter(query)
    articles = wikipedia.search(query_filtered, results=3)
    try:
        for i in range(len(articles)):
            print(f'{articles[i]}, yes?')
            if voice==True:
                text_to_speech(f'{articles[i]}, yes?')
                user_answer = str(speech_to_text())
            else:
                user_answer = input("You:")
            if user_answer.find('no') == -1:            
                article_summary = wikipedia.summary(articles[i], sentences=9)
                nested_dot_filtered = nested_dot_filter(article_summary)
                shortcuts_filtered = shortcuts_filter(nested_dot_filtered)
                before_hyphen_filtered = cut_all_before_hyphen(shortcuts_filtered)
                details_filtered = trim_details(before_hyphen_filtered)
                return trim_length(details_filtered)
        
    except Exception as E:
        print(E)
        return "Temporarily I can't aswer it"
    return "I give up, please ask other question"



