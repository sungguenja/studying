def pi(x):
    return 2*3.14*x

c=list(map(int,input().split(',')))
d=[]
print(c)
for i in range(4):
    d.append(2*3.14*c[i])
print("{}, {}, {}, {}".format(*d, "10.2f"))

asd=list(map(int,input().split(',')))

n=asd[0]
m=asd[1]
zx=[]
for x in range(n):
    zv=[]
    for y in range(m):
        zv.append(x*y)
    zx.append(zv)
print(zx)

zxc=list(map(str, input().split(','' ')))
zxc.sort()
print(",".join(map(str, zxc)))

zvc=list(map(int, input().split(',')))
i=0
while i<len(zvc):
    if zvc[i]%2==0:
        zvc.pop(i)
    else:
        i+=1
print(','.join(map(str, zvc)))

abc=(1,2,3,4,5,6,7,8,9,10)
ab=[]
an=[]
for i in range(0,10):
    if i<5:
        ab.append(abc[i])
    else:
        an.append(abc[i])
ag=tuple(ab)
ah=tuple(an)
print(ag)
print(ah)