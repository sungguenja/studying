a=int(input("what order are u looking 4?"))

if a==1:
    c=[1]
elif a==2:
    c=[1, 1]
else:
    c=[1, 1]
    for i in range(2, a):
        b=c[i-2]+c[i-1]
        c.append(b)

print(c)