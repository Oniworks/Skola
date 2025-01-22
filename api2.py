import requests

response = requests.get("https://httpbin.org/nieeksistee")
print(response.status_code)

if response.status_code == 200:
    print("yes")