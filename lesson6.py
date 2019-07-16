import requests
from bs4 import BeautifulSoup

URL = 'https://www.avito.ru/rossiya?p=1&view=gallery&q=htc'

def get_html(html):
    """Запрос на сайт"""
    r = requests.get(html)
    return r.text


def get_total_pages(html):
    """Возращает количество страниц"""
    soup = BeautifulSoup(html, "lxml")
    pages = soup.find('div', class_="page__footer").find('a',
    class_="toggle-menu__item-link toggle-menu__item-link_pagination toggle-menu__item-link_bordered").get('href')
    total_pages = pages.split('page')[1].split('/')[0]

    return total_pages


def get_page_data(html):

    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find_all('h2', {"class": "post__title"})
    list_name = set()
    for i in h1:
        a = i.find('a').text
        list_name.add(a)
    print(list_name)




def main():
    url = "https://habr.com/top/monthly/"
    dop_url = "page"
    total_pages = get_total_pages(get_html(url)+'page2/')
    get_page_data(url)







if __name__ == "__main__":#точка входа
    main()