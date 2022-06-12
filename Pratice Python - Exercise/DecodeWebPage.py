import requests
from bs4 import BeautifulSoup

webpage = requests.get('https://www.nytimes.com/')
webpage_html = webpage.text
soup = BeautifulSoup(webpage_html, 'html.parser')
for section in soup.find_all('section', {'class': 'story-wrapper'}):
    for title in section.find_all('h3', {'class': 'indicate-hover'}):
        print(title.text)
        print()
