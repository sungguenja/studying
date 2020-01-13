a=int(input("pls input ur num :"))
b=2
c=[]
while a>=1:
    if a%b==1:
        c.append(1)
    else:
        c.append(0)
    a=int(a/b)

print("".join(map(str, c)))