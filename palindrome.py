a=str(input())
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
    print("입력하신 단어는 회문(Palindrome)입니다.")