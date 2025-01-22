import requests

url = "https://api.nationalize.io/?name=Anna"
response = requests.get(url)
results = response.json()
print(results)

for