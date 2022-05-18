import re
from brain.filters import math_symbol_swap

def do_math(query):
    try:
        query_filtered = math_symbol_swap(query)
        remove_not_math_chars = re.compile(r'[0123456789+-/*()]')
        query_filtered_list = remove_not_math_chars.findall(query_filtered)
        query_filtered = ''.join(query_filtered_list)
        #print(eval(query_filtered))
        if (eval(query_filtered)) == 'None' or None:
            return "Powtórz proszę"
        else:
            return str(round(eval(query_filtered), 2))
    except:
        return "Przykro mi. nie umiem tego policzyć"
