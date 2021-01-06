# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import requests, json
url = 'https://eternalreturn-ko.gamepedia.com/'
item = requests.get('http://127.0.0.1:8000/gamedata/')
item = item.json()
write_f = open('item_6th.txt','w',encoding='utf-8')
kinds = [0,'단검','양손검','도끼','쌍검','권총','돌격 소총','저격 소총','레이피어','창','망치','방망이','투척','암기','활','석궁','글러브','톤파','기타','쌍절곤','채찍','머리','옷','팔','다리','장식','음식','음료','설치','재료']
items = ['장미칼','일본도','마사무네','무라마사','바스타드_소드','보검','뚜언_띠엔','플라즈마_소드','경량화_도끼','사신의_낫','대부','피렌체식_쌍검','FN57','더블_리볼버_SP','매그넘-아나콘다','AK-47','M16A1','하푼건','금교전','레일건','매화검','바이던트','파이크','도끼창','강창','모닝_스타','사슴_망치','도깨비_방망이','우산','횃불','슬링','밀가루_폭탄','볼_라이트닝','플러버','가시_탱탱볼','부적','유엽비도','챠크람','매화비표','독침','법륜','플럼바타','컴포지트_보우','강궁','국궁','벽력궁','탄궁','화전','노','저격궁','헤비_크로스보우','철궁','건틀릿','윙_너클','귀골_장갑','벽력귀투','유리_너클','회단_장갑','경찰봉','류큐톤파','루비_스폐셜','험버커_픽업','King-V','노캐스터','슈퍼스트랫','야생마','샤퍼','블리더','바람_채찍','뇌룡편','벽력편','방탄모','소방_헬멧','티아라','왕관','투구','오토바이_헬멧','라이더_자켓','사슬_갑옷','정장','치파오','판금_갑옷','한복','방탄조끼','석양의_갑옷','어사의','검집','금팔찌','바주반드','진홍_팔찌','강철_방패','큐브_워치','부츠','강철_무릎_보호대','풍화륜','매버릭_러너','전투화','킬힐','생명의_가루','우치와','탄창','달빛_펜던트','슈뢰딩거의_상자','진리는_나의_빛','백우선','궁기병의_화살통','감자튀김','구운_감자','구운_붕어','메로구이','뜨거운_라면','모카빵','스크램블_에그','초코칩_쿠키','초코파이_상자','카레','탕약','허니버터','후라이드_치킨','힐링_포션','삶은_달걀','파운드_케이크','카레_고로케','스테이크','구급상자','버터_감자구이','생선까스','볶음라면','냉면','마늘라면','매운탕','대환단','고량주','뜨거운_꿀물','백일취','아메리카노','약주','위스키_콕','정화수','캔_콜라','핫초코','깔루아_밀크','펜듈럼_도끼','지뢰','RDX','미스릴_실','히든_메이든','화염_트랩','생명의_나무','문스톤','독약','모터','미스릴','유리판','이온_전지','VF_혈액_샘플','휴대폰']
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
        left = table_1[1]['title']
        right = table_1[3]['title']
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
    write_f.write("insert into gamedata_item ('name','kinds','rank','max_quantity','stats','material_left','material_right') values ('{0}',{1},2,{5},'{2}',{3},{4});\n".format(name,kind,stat,left,right,cnt))