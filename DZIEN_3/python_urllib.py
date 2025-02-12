import urllib.request
import requests

#pobieranie zwartości strony www i wyświetlanie kodu żródłowego
url = "https://www.python.org"
response = urllib.request.urlopen(url)
html = response.read().decode("utf-8")
# print(html)

#wysyłanie zapytań
request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    headers = response.info()
    print(headers)

print("_"*60)
#pobieranie zawartości strony (requests)

response = requests.get("https://api.github.com/repos/python/cpython")
if response.status_code == 200:
    print(response.json())

#pobieranie obrazu z internetu i zapisywanie go na dysku
image_url = "https://www.python.org/static/community_logos/python-logo.png"
image_response = requests.get(image_url)
if image_response.status_code == 200:
    with open("dimage.png","wb") as file:
        file.write(image_response.content)
    print('Obraz został pobrany i zapisany!')
