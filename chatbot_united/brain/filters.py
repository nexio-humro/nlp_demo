import re
def query_filter(query):
    #classic
    query = re.sub(r"^.+?(?= co )", "", query)
    query = re.sub(r"^.+?(?= powiedz )", "", query)
    query = re.sub(r"^.+?(?= napisz )", "", query)
    query = re.sub(r"^.+?(?= kto )", "", query)
    query = re.sub(r"^.+?(?= kim )", "", query)
    query = re.sub(r"^.+?(?= czy )", "", query)
    query = re.sub(r"^.+?(?= ile )", "", query)
    query = re.sub(r"^.+?(?= jak )", "", query)
    query = re.sub(r"^.+?(?= wiek )", "", query)
    query = re.sub(r"^.+?(?= kiedy )", "", query)
    query = re.sub(r"^.+?(?= autor )", "", query)
    query = query.replace("co to jest ", "")
    query = query.replace("napisz mi kto ", "")
    query = query.replace("powiedz mi kto ", "")
    query = query.replace("napisz mi ", "")
    query = query.replace("powiedz mi ", "")
    query = query.replace("no dobra ", "")
    query = query.replace("kim jest ", "")
    query = query.replace("czy wiesz ", "")
    query = query.replace("kto to jest ", "")
    query = query.replace("kto jest ", "")
    query = query.replace("kto to był ", "")
    #age
    query = query.replace("ile lat ma", "")
    query = query.replace("ile lat", "")
    query = query.replace("jak stary jest", "")
    query = query.replace("wiek", "")
    query = query.replace("kiedy była", "")
    query = query.replace("kiedy miała miejsce", "")
    #place
    query = query.replace("gdzie jest ", "")
    query = query.replace("gdzie leży ", "")
    
    #books
    query = query.replace("kto napisał", "")
    query = query.replace("autor", "")
    query = query.replace("autorem", "")
    query = query.replace("autorką", "")
    query_filtered = query.lstrip()
    return query_filtered


def math_symbol_swap(query):
    query = query.replace("jeden", "1")
    query = query.replace("pierwszej", "1")
    
    query = query.replace("dwa", "2")
    query = query.replace("drugiej", "2")
    query = query.replace("trzeciej", "3")
    query = query.replace("czwartej", "4")
    query = query.replace("piątej", "5")
    query = query.replace("szóstej", "6")
    query = query.replace("siódmej", "7")
    query = query.replace("ósmej", "8")
    query = query.replace("dziewiątej", "9")
    query = query.replace("dziesiątej", "10")

    query = query.replace("dodać", "+")
    query = query.replace("dodac", "+")
    query = query.replace("do potęgi", "**")
    query = query.replace("do potegi", "**")
    query = query.replace("^", "**")
    query = query.replace("do ", "**")
    query = query.replace("plus", "+")
    query = query.replace("minus", "-")
    query = query.replace("odjąć", "-")
    query = query.replace("odjac", "-")
    query = query.replace("podzielić", "/")
    query = query.replace("podzielic", "/")
    query = query.replace("razy", "*")
    query = query.replace("x", "*")
    query_filtered = query.lstrip()
    return query_filtered


def currency_symbol_swap(query):
    #currency
    query = query.replace("franki szwajcarskie", "CHF")
    query = query.replace("frank szwajcarski", "CHF")
    query = query.replace("euro", "EUR")
    query = query.replace("dolary amerykańskie", "USD")
    query = query.replace("dolar amerykański", "USD")
    query = query.replace("dolary kanadyjskie", "CAD")
    query = query.replace("dolar kanadyjski", "CAD")
    query = query.replace("funty szterlingi", "GBP")
    query = query.replace("funt szterling", "GBP")
    query = query.replace("funty angielskie", "GBP")
    query = query.replace("funt angielski", "GBP")
    query = query.replace("funty brytyjskie", "GBP")
    query = query.replace("funt brytyjski", "GBP")
    query = query.replace("funty", "GBP")
    query = query.replace("funt", "GBP")
    query = query.replace("dolar kanadyjski", "CAD")
    query = query.replace("jeny japońskie", "JPY")
    query = query.replace("jen japoński", "JPY")
    
    query_filtered = query.lstrip()
    
    return query_filtered

def nested_dot_filter(sentences):
    trimmed_sentences = re.sub("[\(\[].*?[\)\]]", "", sentences)
    trimmed_sentences = trimmed_sentences.replace(")", "").replace("(", "")
    return trimmed_sentences

def commas_to_dots(sentences):
    sentences_filtered = sentences.replace(",", ".")
    return sentences_filtered