import requests
import concurrent.futures
from DaftarKecamatan import kec
import time

cities = kec

def request_weather(city):
    try:
        key = 'get API on weatherapi.com'
        api = 'http://api.weatherapi.com/v1/current.json'
        payload = {
            "key": key,
            "q": city,
            "aqi": 'no'
        }
        response = requests.get(api, params=payload, timeout=1000)
        data = response.json()
        print(f"Weather in {city}: {data['current']['condition']['text']}, Temperature: {data['current']['temp_c']} C")
    except Exception as e:
        print(f"Failed to retrieve weather for {city}: {e}")

def main():
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(request_weather, cities)

    print(f"Total execution time: {time.time() - start_time}")

if __name__ == '__main__':
    main()
