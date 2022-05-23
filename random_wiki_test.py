import wikipedia
import re


def nested_dot_filter(sentences):
    trimmed_sentences = re.sub("[\(\[].*?[\)\]]", "", sentences)
    trimmed_sentences = trimmed_sentences.replace(")", "").replace("(", "")
    return trimmed_sentences

def trim_details(sentences):
    trimmed_sentences = re.sub("[\==\[].*?[\==\]]", "", sentences)
    trimmed_sentences = trimmed_sentences.replace("==", "").replace("==", "")
    return trimmed_sentences

def wiki_shortcuts_filter(article):
    article = article.replace(" r.", " roku")
    article = article.replace(" dn.", " dniach")
    article = article.replace(" ur.", " urodzony")
    article = article.replace(" wlaśc.", " właściwie")
    article = article.replace(" właśc.", " właściwie")
    article = article.replace(" właść.", " własciwie")
    article = article.replace(" duń.", " duński")
    article = article.replace(" duń.", " duński")
    article = article.replace(" ros.", " rosyjski")
    article = article.replace(" ps.", " pseudonim")
    article = article.replace(" j.a", " jednostka astronomiczna")
    article = article.replace(" gen.", " generał")
    return article

def cut_all_before_hyphen(article):
    article_splitted = article.split("– ")
    print(len(article_splitted))
    if len(article_splitted)>1:
        article_splitted.pop(0)
        filtered = '–'.join(article_splitted)
        return filtered
    else:
        return article

wikipedia.set_lang('pl')
try:
    # random_article = wikipedia.random(pages=1)
    random_article = wikipedia.search("seksmisja", results=1)
except:
    print('cos nie pyklo')
article_summary = wikipedia.summary(random_article, sentences=6)
print('SUMMARY ' + article_summary)


nested_dot_filtered = nested_dot_filter(article_summary)
print('FIRST po filtracji nested ' + nested_dot_filtered)
shortcuts_filtered = wiki_shortcuts_filter(nested_dot_filtered)
print('SECOND po filtracji shortcuts' + shortcuts_filtered)
before_hyphen_filtered = cut_all_before_hyphen(shortcuts_filtered)

print('THIRD po ucieciu myslnika' + before_hyphen_filtered)

details_filtered = trim_details(before_hyphen_filtered)
print(details_filtered)




def trim_length(filtered_article):
    sentences_splitted = filtered_article.split(".")
    # print('sentences splitted:', sentences_splitted)
    total_words = 0
    article_ordered = ''
    
    # while (total_words < 15):
    for sentence in sentences_splitted:
        # while ((total_words < 9) and not (sentence + '.' == article_ordered)):
        if total_words < 5:
            # print('sentence: ',sentence + '.')
            words = sentence.split(" ")
            total_words = total_words + len(words)
            print(total_words)
            # print(sentence)
            article_ordered+=sentence
            article_ordered+='.'
            # print('artykul: ', article_ordered)

    return article_ordered


trim_length(details_filtered)
print(trim_length(details_filtered))

