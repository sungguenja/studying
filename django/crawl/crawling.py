import requests
import csv
from bs4 import BeautifulSoup


def get_html():
    adress = 'https://namu.wiki/w/%EB%8F%99%EB%AC%BC%EC%9D%98%20%EC%88%B2%20%EC%8B%9C%EB%A6%AC%EC%A6%88/%EB%85%B8%EB%9E%98%20%EB%AA%A9%EB%A1%9D'

    return requests.get(adress).text

def crawl():
    page = []

    c = get_html()

    soup=BeautifulSoup(c)

    for tag in soup.select('td'):
        if tag.text != 'O':
            page.append(tag.text + '\n')
    return page

now_data = crawl()

my_file = open('data5.txt','w', encoding='utf-8')
for dt in now_data:
    my_file.write(dt + '\n')
