a=[1, 2, 3, 4, 3, 2, 1]
i=0
while i<len(a):
    j=i+1
    while j<len(a):
        if a[i]==a[j]:
            a.pop(j)
        else:
            j=j+1
    i=i+1
print(a)

b=[2, 4, 6, 8, 10]
n, m = 0, 0
for i in range(5):
    if b[i]==5:
        n+=1
    if b[i]==10:
        m+=1

if n==0:
    print("5 => False")
else:
    print("5 => true")

if m==0:
    print("10 => false")
else:
    print("10 => True")

def square(x):
    return x**2

c,d=map(int,input().split(','))

print("square({0}) => {1}".format(c, square(c)))
print("square({0}) => {1}".format(d, square(d)))

e, f = map(str, input().split(','' '))
if len(e)>len(f):
    print(e)
else:
    print(f)