import requests
import bs4

response = requests.get("https://en.wikipedia.org/wiki/Kermode_bear")

if response.status_code == 200:
    page_content = response.text
    soup = bs4.BeautifulSoup(page_content, 'html.parser')

    # soup.a only gets you the first link...

    links = soup.find_all('a')

    for i in links:
        print(i.get("href"))



else:
    print("Status Code" + response.status_code)