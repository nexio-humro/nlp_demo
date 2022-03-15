import re
from brain.filters import query_filter


def do_math(query):
    try:
        query_filtered = query_filter(query)
        remove_not_math_chars = re.compile(r'[0123456789+-/*()]')
        query_filtered_list = remove_not_math_chars.findall(query_filtered)
        query_filtered = ''.join(query_filtered_list)
        print(eval(query_filtered))
    except:
        pass