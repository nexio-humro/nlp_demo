import re
def query_filter(query):
    #classic
    query = query.replace("co to jest ", "")
    query = query.replace("napisz mi kto ", "")
    query = query.replace("powiedz mi kto ", "")
    query = query.replace("napisz mi ", "")
    query = query.replace("powiedz mi ", "")
    query = query.replace("no dobra ", "")
    query = query.replace("kim jest ", "")
    query = query.replace("czy wiesz ", "")
    query = query.replace("kto to jest ", "")
    query = query.replace("kto to był ", "")
    #age
    query = query.replace("ile lat ma", "")
    query = query.replace("ile lat", "")
    query = query.replace("jak stary jest", "")
    query = query.replace("wiek", "")
    query = query.replace("kiedy była", "")
    query = query.replace("kiedy miała miejsce", "")
    #math
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
    
    #books
    query = query.replace("kto napisał", "")
    query = query.replace("autor", "")
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