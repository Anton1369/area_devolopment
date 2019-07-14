import requests
from bs4 import BeautifulSoup



def word():
    url = "https://nekdo.ru/random/"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    response = soup.find('div', class_='text').text
    return response