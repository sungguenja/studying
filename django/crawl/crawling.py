import requests
import csv
from bs4 import BeautifulSoup


def get_html(url):
    html=""
    res = requests.get(url)

    if res.status_code == 200:
        html = res.text
    
    return html

def crawl(url):
    page = []

    c = get_html(url)

    soup=BeautifulSoup(c,'html.parser')

    for tag in soup.select('table[class=wiki-table]'):
        if tag.text != '':
            page.append(tag.text + '\n')
        else:
            try:
                img = tag.find('img')
                page.append(img.get('src'))
            except AttributeError:
                continue
    
    return page

now_data = crawl('')

my_file = open('data4.txt','w', encoding='utf-8')
for dt in now_data:
    my_file.write(dt + '\n')

my_file.close()