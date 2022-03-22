import time


def which_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    return current_time
