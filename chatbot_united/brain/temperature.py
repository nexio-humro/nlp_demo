
API_KEY = '03566fc33237e41a2b6d76f954ed7191'
import json
import requests

def get_temperature():
    city = input("You:")
    name2geo = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&lang=pl&limit=3&appid={API_KEY}'
    geo_response = requests.get(name2geo)
    geo_response = geo_response.json()
    # print('geo response: ', geo_response[0]["name"])
    try:
        lat = geo_response[0]["lat"]
        lon = geo_response[0]["lon"]
        # print(lat, lon)
        geo2temp = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}'

        temp_response = requests.get(geo2temp)
        temp_response = temp_response.json()
        # print('temp response: ', temp_response["name"])
        # print(temp_response["main"]["temp"])
        temperature = temp_response["main"]["temp"]
    except:
        temperature = 'xdd'
    return temperature

def show_temperature():
    temperature = get_temperature()
    # print(f'temperatura:{temperature}')
    if temperature != 'xdd':
        temperature = round(temperature, 1)
        return f'Z tego co mi wiadomo w tym momencie wynosi {temperature} stopni Celciusza'
    else:
        return 'Nie znam tego miasta'

