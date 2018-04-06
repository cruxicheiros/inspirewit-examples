import requests
import bs4

base_url = "https://duckduckgo.com/"

search_term = input("Search something >>  ")

response = requests.get(base_url, params={'q' : search_term})

if response.status_code == 200:
    page_content = response.text
    soup = bs4.BeautifulSoup(page_content, 'html.parser')

    print(soup.prettify())

    # What goes here...

else:
    print("Status Code" + response.status_code)