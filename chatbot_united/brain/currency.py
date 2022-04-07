from forex_python.converter import CurrencyRates
from brain.filters import currency_symbol_swap
from brain.voice import text_to_speech, speech_to_text

def get_rate_x_to_pln(query, voice):
    if voice==True:
        text_to_speech("Potwierdź proszę na jaką walutę mam przeliczyć złotówkę")
    print("Potwierdz proszę na jaką walutę mam przeliczyć złotówkę")
    if voice==True:
        user_answer = str(speech_to_text())
    else:
        user_answer = input("You:")
    query_filtered = currency_symbol_swap(user_answer)
    print('query filered:' + query_filtered)
    c = CurrencyRates()
    try:
        return f"Obecny kurs {query_filtered} to {round(c.get_rate(query_filtered, 'PLN'), 2)} złotego"
    except:
        return "Niestety w chwili obecnej nie mam dostępu do tej informacji"