asd = {"afafaf": 2000, "ggd": 1514, "zxcv": 12414, "gbzx": 124213, "nnm": 212, "gsdf": 1234}

b=list(dict.keys(asd))
c=list(dict.values(asd))
i=0
j=i+1
while i < len(b):
    while j < len(b):
        if c[i] < c[j]:
            save1=b[i]
            b[i]=b[j]
            b[j]=save1
            save2=c[i]
            c[i]=c[j]
            c[j]=save2
        else:
            j+=1
    i+=1
    j=i+1
d=dict.fromkeys(b)
for i in b:
    d[i]=asd[i]
print(d)

aa = {'ice coffee': 1900, 'cafe mocha': 3300, 'Espresso': 1900, 'cafe latte': 2500, 'cappuccino': 2500, 'vanila latte': 2900}
 

bb = {'Hazelnuts latte': 2900, 'cafe mocha': 3300, 'milk coffe': 3300, 'ice coffee': 1900, 'green tea': 3300}

ak=list(dict.keys(aa))
bk=list(dict.keys(bb))
i=0
j=0

while i < len(ak):
    if aa[ak[i]]<3000:
        ak.pop(i)
    else:
        i+=1
while j < len(bk):
    if bb[bk[j]]<3000:
        bk.pop(j)
    else:
        j+=1
i=0
j=0
while i<len(ak):
    while j<len(bk):
        if str(ak[i])==str(bk[j]):
            bk.pop(j)
        else:
            j+=1
    i+=1
    j=0
i,j=0,0
ck=ak+bk
cv=[]
for i in range(len(ak)):
    cv.append(aa[ak[i]])
for j in range(len(bk)):
    cv.append(bb[bk[j]])
cc=dict.fromkeys(ck)
for i in range(len(ck)):
    cc[ck[i]]=cv[i]
print(cc)

fruit = ['   apple    ','banana','  melon']
f1=list(fruit[0])
f2=list(fruit[1])
f3=list(fruit[2])
i=0
while i<len(f1):
    if f1[i]==' ':
        f1.pop(i)
    else:
        i+=1
fruit_2={'apple': len(f1), 'banana': len(f2), 'melon': len(f3)}
print(fruit_2)

beer = {'kloud': 2000, 'fox': 2100, 'blanc': 2500, 'wine': 4000, 'fire': 500}
beer_keys = list(dict.keys(beer))

beer_up = dict.fromkeys(beer)
for i in range(len(beer_keys)):
    beer_up[beer_keys[i]]=beer[beer_keys[i]]*1.05
print(beer_up)