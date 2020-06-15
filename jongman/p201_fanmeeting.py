def fanmeeting(artist,audience):
    cnt = 0
    artists = int(artist.replace('F','0').replace('M','1'),2)
    audiences = int(audience.replace('F','0').replace('M','1'),2)
    for _ in range(len(audience)-len(artist)+1):
        if not artists & audiences:
            cnt += 1
        artists = artists<<1
    return cnt
    
for t in range(1,int(input())+1):
    idol = input()
    fan = input()
    print(fanmeeting(idol,fan))