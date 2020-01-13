for i in range(1, 5, 1):
    print("*" * i)
print()

n=1
while n<5:
    print("*" * n)
    n=n+1
print()

for a in range(1,3):
    for b in range(1,5):
        print("*" * b)
print()

c, d = 1, 1
while c<=2:
    while d<=4:
        print("*" * d)
        d+=1
    c+=1
    d=1
print()

e, f = 5, 1
while e >= 0:
    print("{0}{1}".format(" "*e, "*"*(2*f-1)))
    e -= 1
    f += 1

g, h= 7, 0
while g>=0:
    print("{0}{1}{0}".format(" "*h, "*"*g))
    g-=2
    h+=1
