import requests
from DaftarKecamatan import kec

cities = kec

def request_weather(city):
    key = 'get API on weatherapi.com'
    city = city
    api = 'http://api.weatherapi.com/v1/current.json'
    payload = {
        "key": key,
        "q": city,
        "aqi": 'no'
    }
    response = requests.get(api, params=payload, timeout=1000)
    print(response.json())

def main():
    for city in cities:
        request_weather(city)

if __name__ == '__main__':
    main()