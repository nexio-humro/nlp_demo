import translators


def translate_to_english(phrase):
    translated = translators.google(phrase, to_language = 'en')
    return translated

def translate_to_polish(phrase):
    translated = translators.google(phrase, to_language = 'pl')
    return translated

print(translate_to_english('Ok, muszę zweryfikować Twoją tożsamość. Pokaż proszę dowód osobisty do kamery.'))
print(translate_to_english('Proces uczenia jest głęboki, ponieważ struktura sztucznych sieci neuronowych składa się z wielu warstw wejściowych, wyjściowych i ukrytych.'))

 