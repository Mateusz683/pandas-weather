from http.client import responses

from config import Settings
import requests
import datetime

def fetch_weather():
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={Settings.city}&appid={Settings.api_key}"

    try:
        response = requests.get(URL)
        weather = response.json()
        now = datetime.datetime.now()

        data = {
            "Odczuwalna" : weather["main"]["feels_like"],
            "Ciśnienie" : weather["main"]["pressure"],
            "Wilgotność" : weather["main"]["humidity"],
            "Zwykła temperatura" : weather["main"]["temp"],
            "Opis Pogody" : weather["weather"][0]["description"],
            "Miejsce": weather["name"],
            "Prędkość wiatru": weather["wind"]["speed"],
            "Czas pobrania pomiaru" : now.strftime("%Y-%m-%d %H:%M:%S")
        }
        return(data)
    except:
        print("wystąpił błąd")



