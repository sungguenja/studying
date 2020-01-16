a=str(input("input ur word"))
b=list(map(str,a))
b.reverse()
c=list(map(str,b))
b.reverse()
d=0

for i in range(0,len(b),1):
    if str(b)==str(c):
        d+=1

if d==len(b):
    print(a)
    print("your word is Palindrome")
else:
    print("your word is not palindrome")