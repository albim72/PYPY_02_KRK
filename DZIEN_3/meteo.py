latitude = 51.5074
longitude = -0.1278
weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
weather_response = requests.get(weather_url)
if weather_response.status_code == 200:
    weather_data = weather_response.json()
    print("Weather in London:", weather_data["current_weather"])
else:
    print("Error fetching weather data")

# 5. Obsługa błędów i timeout w zapytaniach API
try:
    response_timeout = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=5)
    response_timeout.raise_for_status()  # Rzuca wyjątek przy błędzie HTTP
    print("Response with Timeout Handling:", response_timeout.json())
except requests.exceptions.RequestException as e:
    print("Error:", e)
