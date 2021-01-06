# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import requests, json
url = 'https://eternalreturn-ko.gamepedia.com/'
item = requests.get('http://127.0.0.1:8000/gamedata/')
item = item.json()
write_f = open('item_9th.txt','w',encoding='utf-8')
kinds = [0,'단검','양손검','도끼','쌍검','권총','돌격 소총','저격 소총','레이피어','창','망치','방망이','투척','암기','활','석궁','글러브','톤파','기타','쌍절곤','채찍','머리','옷','팔','다리','장식','음식','음료','설치','재료']
items = ['프라가라흐','레바테인','다인슬라이프','악켈테','사사성광','미스틸테인','화첨창','롱기누스의_창','여의봉','수다르사나','만천화우','페일노트','샤릉가','월계관','불꽃_드레스','카바나','퀸_오브_하트','스카디의_팔찌','레이더','오토-암즈','EOD_부츠','분홍신','글레이셜_슈즈','헤르메스의_부츠','에메랄드_타블렛','리모트_마인','스마트_폭탄']
print(len(items))
for j in range(len(items)):
    item_html = requests.get(url+items[j])
    item_html = bs(item_html.text,'html.parser')
    tables = item_html.find_all('table')
    if len(tables) == 0:
        print(items[j])
        continue
    item_stat = tables[0].find_all('center')
    name = item_stat[0].get_text()
    cnt = 1
    try:
        kind = item_stat[1].find('a').get_text()
    except AttributeError:
        print(items[j])
        continue
    kind = kinds.index(kind)
    stats = tables[0].find_all('li')
    stat = {}
    for i in range(len(stats)):
        stats_text = stats[i].get_text()
        if '+' in stats_text:
            key,value = stats_text.split('+')
            key = key[:-1]
            key = '"{}"'.format(key)
            value = '+'+value
            value = '"{}"'.format(value)
            stat[key] = value
        elif '-' in stats_text:
            key,value = stats_text.split('-')
            key = key[:-1]
            value = '-'+value
            key = '"{}"'.format(key)
            value = '"{}"'.format(value)
            stat[key] = value
    table_1 = tables[1].find_all('a')
    try:
        left = table_1[2].get_text()
        right = table_1[4].get_text()
    except KeyError:
        print(items[j])
        continue
    for i in range(len(item)):
        if item[i]['fields']['name'] == left:
            left = item[i]['pk']
        if item[i]['fields']['name'] == right:
            right = item[i]['pk']
        if type(left) == int and type(right) == int:
            break
    if kind == 29:
        cnt = 3
    elif kind == 26 or kind == 27 or kind == 28:
        cnt = 5
    write_f.write("insert into gamedata_item ('name','kinds','rank','max_quantity','stats','material_left','material_right') values ('{0}',{1},4,{5},'{2}',{3},{4});\n".format(name,kind,stat,left,right,cnt))