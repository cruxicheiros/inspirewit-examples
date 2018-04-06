import requests
import bs4

response = requests.get("https://en.wikipedia.org/wiki/Kermode_bear")
base_url = "https://en.wikipedia.org"

if response.status_code == 200:
    page_content = response.text
    soup = bs4.BeautifulSoup(page_content, 'html.parser')

    links = soup.find_all('a')

    for i in links:
        url = i.get("href")  # No Problem

        if isinstance(url, str):
            if url[:6] == "/wiki/":
                if ':' not in url:
                    print(base_url + url)

        else:
            print('No href attribute found')

else:
    print("Status Code" + response.status_code)