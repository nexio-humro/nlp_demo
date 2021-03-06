import wikipedia
from brain.filters import nested_dot_filter, query_filter, cut_all_before_hyphen, shortcuts_filter, trim_details, trim_length
from brain.voice import text_to_speech, speech_to_text
wikipedia.set_lang("pl")


def wikipedia_search(query, voice):
    query_filtered = query_filter(query)
    articles = wikipedia.search(query_filtered, results=3)
    try:
        for i in range(len(articles)):
            print(f'{articles[i]}, tak?')
            if voice==True:
                text_to_speech(f'{articles[i]}, tak?')
                user_answer = str(speech_to_text())
            else:
                user_answer = input("You:")
            if user_answer.find('nie') == -1:            
                article_summary = wikipedia.summary(articles[i], sentences=9)
                nested_dot_filtered = nested_dot_filter(article_summary)
                shortcuts_filtered = shortcuts_filter(nested_dot_filtered)
                before_hyphen_filtered = cut_all_before_hyphen(shortcuts_filtered)
                details_filtered = trim_details(before_hyphen_filtered)
                return trim_length(details_filtered)

                # article_summary = article_summary.split("– ")
                # article_summary = article_summary[1]
                # article_summary = article_summary.split("=")
                # article_summary = article_summary[0]
                # article_filtered = nested_dot_filter(article_summary)
                # article_filtered_splitted = article_filtered.split(".")
                # first_sentence_splitted = article_filtered_splitted[0].split()
                # if len(first_sentence_splitted) > 15:
                #     answer = article_filtered_splitted[0]
                #     return answer
                #     break
                # elif len(article_filtered_splitted)>=3:
                #     answer = article_filtered_splitted[0] + '.' + article_filtered_splitted[1] + '.' + article_filtered_splitted[2] + '.'
                #     # print(answer)

                #     return answer
                    
                #     break
                # else:
                #     for s in range(len(article_filtered_splitted)):
                #         answer = article_filtered_splitted[s] + '.'
                #         # print(answer)
                #         return answer
                #         break
    except Exception as E:
        print(E)
        return "Chwilowo nie jestem w stanie odpowiedzieć"

    return "Poddaję się, zadaj proszę inne pytanie"


    #     print("Poddaję się, zadaj proszę inne pytanie")
    #     if voice==True:
    #         text_to_speech("Poddaję się. zadaj proszę inne pytanie")
    # except Exception as E:
    #     print(E)
    #     print("Poddaję się, zadaj proszę inne pytanie")
    #     if voice==True:
    #         text_to_speech("Poddaję się. zadaj proszę inne pytanie")


