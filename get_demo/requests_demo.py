import requests

response = requests.get("https://en.wikipedia.org/wiki/Kermode_bear")

print(response.status_code)
print(response.text)