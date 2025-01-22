import requests

response = requests.get("https://v2.jokeapi.dev/joke/Programming?type=single")
print(response.status_code)
print(response.json())