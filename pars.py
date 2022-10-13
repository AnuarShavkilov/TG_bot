import requests
from bs4 import BeautifulSoup


HOST = 'https://9v.ru'
word = input()
url = f'https://9v.ru/search?q={word}&lang=ru'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all('div', class_='product-preview__content')

for link in quotes:
    links = HOST+link.find('div', class_='product-preview__title').find('a').get('href')
    print(links)



