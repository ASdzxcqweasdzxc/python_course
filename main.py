import requests

s = requests.get("https://github.com")
print(s.headers)
