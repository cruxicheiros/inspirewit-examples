import requests
import bs4

response = requests.get("https://en.wikipedia.org/wiki/Kermode_bear")

if response.status_code == 200:
    page_content = response.text
    soup = bs4.BeautifulSoup(page_content, 'html.parser')

    print("soup.title:              ", soup.title)
    print("soup.title.string:       ", soup.title.string)

    print("\nsoup.a:                  ", soup.a)

else:
    print("Status Code" + response.status_code)