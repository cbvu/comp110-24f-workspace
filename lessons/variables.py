def get_weather_report() -> str:
    weather: str = input("What's the weather like today? ")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather")
    return weather


get_weather_report()
