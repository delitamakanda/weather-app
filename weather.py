import requests

def get_weather_forcast():
    #connection to api weather
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Paris,fr&units=metric&APPID=3ba2c45e305b029f81b09ea06e2907e1'
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    forcast = 'La météo du jour est '
    forcast += description + ' avec une température haute de ' + str(int(temp_max)) + '°'
    forcast += ' et une température basse de ' + str(int(temp_min)) + '°.'

    return forcast
