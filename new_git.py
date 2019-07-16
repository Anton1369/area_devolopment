import requests
from bs4 import BeautifulSoup


def response():
    html = "https://habr.com/ru/top/"
    req = requests.get(html).text
    soup = BeautifulSoup(req, "lxml")
    r = soup.find('div', class_="posts_list").find_all('h2', class_="post__title")
    l = []
    for i in r:
        a = i.find('a', class_='post__title_link').get("href")
        l.append(a)
    return l
print(response())