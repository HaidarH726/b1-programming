import requests
import time
import json

url = "https://api.open-meteo.com/v1/forecast"
eu_capitals = [
{"city": "Vienna", "country": "Austria",
"lat": 48.2082, "lon": 16.3738},
{"city": "Brussels", "country": "Belgium",
"lat": 50.8503, "lon": 4.3517},
{"city": "Sofia", "country": "Bulgaria",
"lat": 42.6977, "lon": 23.3219},
{"city": "Zagreb", "country": "Croatia",
"lat": 45.8150, "lon": 15.9819},
{"city": "Nicosia", "country": "Cyprus",
"lat": 35.1856, "lon": 33.3823},
{"city": "Prague", "country": "Czechia",
"lat": 50.0755, "lon": 14.4378},
{"city": "Copenhagen", "country": "Denmark",
"lat": 55.6761, "lon": 12.5683},
{"city": "Tallinn", "country": "Estonia",
"lat": 59.4370, "lon": 24.7536},
{"city": "Helsinki", "country": "Finland",
"lat": 60.1695, "lon": 24.9354},
{"city": "Paris", "country": "France",
"lat": 48.8566, "lon": 2.3522},
{"city": "Berlin", "country": "Germany",
"lat": 52.5200, "lon": 13.4050},
{"city": "Athens", "country": "Greece",
"lat": 37.9838, "lon": 23.7275},
{"city": "Budapest", "country": "Hungary",
"lat": 47.4979, "lon": 19.0402},
{"city": "Dublin", "country": "Ireland",
"lat": 53.3498, "lon": -6.2603},
{"city": "Rome", "country": "Italy",
"lat": 41.9028, "lon": 12.4964},
{"city": "Riga", "country": "Latvia",
"lat": 56.9496, "lon": 24.1052},
{"city": "Vilnius", "country": "Lithuania",
"lat": 54.6872, "lon": 25.2797},
{"city": "Luxembourg", "country": "Luxembourg",
"lat": 49.6116, "lon": 6.1319},
{"city": "Valletta", "country": "Malta",
"lat": 35.8989, "lon": 14.5146},
{"city": "Amsterdam", "country": "Netherlands",
"lat": 52.3676, "lon": 4.9041},
{"city": "Warsaw", "country": "Poland",
"lat": 52.2297, "lon": 21.0122},
{"city": "Lisbon", "country": "Portugal",
"lat": 38.7223, "lon": -9.1393},
{"city": "Bucharest", "country": "Romania",
"lat": 44.4268, "lon": 26.1025},
{"city": "Bratislava", "country": "Slovakia",
"lat": 48.1486, "lon": 17.1077},
{"city": "Ljubljana", "country": "Slovenia",
"lat": 46.0569, "lon": 14.5058},
{"city": "Madrid", "country": "Spain",
"lat": 40.4168, "lon": -3.7038},
{"city": "Stockholm", "country": "Sweden",
"lat": 59.3293, "lon": 18.0686}
]
weather_data = {}

for capital in eu_capitals:

    parameters = {
        "latitude": capital["lat"],
        "longitude": capital["lon"],
        "current_weather": True,
        "hourly": "temperature_2m,precipitation_probability,weathercode"
    }

    response = requests.get(url, params=parameters)

    print(f"\nCity: {capital['city']}")
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        weather_data[capital["city"]] = {
            "country": capital["country"],
            "coordinates": {
                "latitude": capital["lat"],
                "longitude": capital["lon"]
            },
            "current_weather": data.get("current_weather")
        }
    else:
        print("Failed to fetch data")

    time.sleep(0.7)

print("Current Weather:")
print(data.get("current_weather"))



with open("eu_weather_data.json", "w") as f:
    json.dump(weather_data, f, indent=4)

print("\nData saved to eu_weather_data.json")