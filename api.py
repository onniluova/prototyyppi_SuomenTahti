import requests

def palautaSääKohteesta(kaupunki):
    api_avain = "64a3c819f71b57b32d2758c31a6dcfa9"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_avain}"
    vastaus = requests.get(url)
    weather_data = vastaus.json()
    return weather_data["weather"][0]["main"]