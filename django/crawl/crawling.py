import requests
import csv
from bs4 import BeautifulSoup


def get_html():
    adress = 'https://api.themoviedb.org/3/search/movie?api_key='
    res = requests.get(adress+key+'&query='+'스파이더맨 뉴 유니버스')
    movie_id = res.json()['results'][0]['id']
    return movie_res.json().get('posters')

# def crawl(url):
#     page = []

#     c = get_html(url)

#     soup=BeautifulSoup(c,'html.parser')

#     for tag in soup.select('table[class=wiki-table]'):
#         if tag.text != '':
#             page.append(tag.text + '\n')
#         else:
#             try:
#                 img = tag.find('img')
#                 page.append(img.get('src'))
#             except AttributeError:
#                 continue
    
#     return page

# now_data = crawl('')

# my_file = open('data4.txt','w', encoding='utf-8')
# for dt in now_data:
#     my_file.write(dt + '\n')

# my_file.close()
print(get_html())