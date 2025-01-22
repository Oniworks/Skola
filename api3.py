import requests

response = requests.get("https://v2.jokeapi.dev/joke/Programming?type=single")

if response.status_code == 200:
    atbilde = response.json()
    print(atbilde["joke"])
    print(atbilde["flags"]["religious"]) #For getting into the second layer
    print(atbilde["id"])