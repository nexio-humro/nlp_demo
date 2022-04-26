import time


def get_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    return current_time

def get_weekday():
    t = time.localtime()
    current_weekday = time.strftime("%A", t)
    if current_weekday == 'Monday':
        current_weekday = 'poniedziałek'
    elif current_weekday == 'Tuesday':
        current_weekday = 'wtorek'
    elif current_weekday == 'Wednesday':
        current_weekday = 'środa'
    elif current_weekday == 'Thursday':
        current_weekday = 'czwartek'
    elif current_weekday == 'Friday':
        current_weekday = 'piątek'
    elif current_weekday == 'Saturday':
        current_weekday = 'sobota'
    elif current_weekday == 'Sunday':
        current_weekday = 'niedziela'
    return current_weekday

