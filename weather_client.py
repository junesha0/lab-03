import requests
from typing import Dict

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"
JOKEURL = "https://official-joke-api.appspot.com"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "f810fae88cef4ec775895ca44a5cc23b"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()

# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)
def get_rand_joke():
    url = JOKEURL + "/random_joke"
    Joke = requests.get(url)
    return Joke.json()

def main():
    temp = get_weather("London")
    print(temp, "\n")
    joke = get_rand_joke()
    print(joke)

if __name__ == "__main__":
    main()
