dicBase = (('가','깋'), ('나','닣'), ('다','딯'), ('라','맇'), ('마','밓'), ('바','빟'), ('사','싷'), ('아','잏'), ('자','짛'), ('차','칳'), ('카','킿'), ('타','팋'), ('파','핗'), ('하','힣'))
 

inputWord = ['막', '부모님', '비용', '비행기', '원래', '처리', '최초', '꼴', '좀', '들다', '싶다', '수출', '계시다', '다', '뒤', '듣다', '함께', '아이', '무척', '보이다', '가지다', '그', '자르다', '데리다', '마리', '개', '정도', '옳다', '놀이','뜨겁다']

ga = []
na = []
da = []
la = []
ma = []
ba = []
sa = []
aa = []
ja = []
ca = []
ka = []
ta = []
pa = []
ha = []
di = [ga,na,da,la,ma,ba,sa,aa,ja,ca,ta,pa,ha]
for i in range(len(inputWord)):
    ff = list(inputWord[i])
    if ord(ff[0]) >= ord('하'):
        ha.append(inputWord[i])
    elif ord(ff[0]) >= ord('파'):
        pa.append(inputWord[i])
    elif ord(ff[0]) >= ord('타'):
        ta.append(inputWord[i])
    elif ord(ff[0]) >= ord('카'):
        ka.append(inputWord[i])
    elif ord(ff[0]) >= ord('차'):
        ca.append(inputWord[i])
    elif ord(ff[0]) >= ord('자'):
        ja.append(inputWord[i])
    elif ord(ff[0]) >= ord('아'):
        aa.append(inputWord[i])
    elif ord(ff[0]) >= ord('사'):
        sa.append(inputWord[i])
    elif ord(ff[0]) >= ord('바'):
        ba.append(inputWord[i])
    elif ord(ff[0]) >= ord('마'):
        ma.append(inputWord[i])
    elif ord(ff[0]) >= ord('라'):
        la.append(inputWord[i])
    elif ord(ff[0]) >= ord('다'):
        da.append(inputWord[i])
    elif ord(ff[0]) >= ord('나'):
        na.append(inputWord[i])
    elif ord(ff[0]) >= ord('가'):
        ga.append(inputWord[i])
print(di)