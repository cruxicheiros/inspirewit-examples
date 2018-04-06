import requests
import bs4

response = requests.get("https://en.wikipedia.org/wiki/Kermode_bear")
page_content = response.text

soup = bs4.BeautifulSoup(page_content, 'html.parser')

print(soup)

# soup.prettify(): adds indentation
# soup.find_all(): finds all of a particular element
