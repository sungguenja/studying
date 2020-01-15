# aq=[]
# for i in range(2):
#     aw=[]
#     for j in range(3):
#         ae=[]
#         for k in range(4):
#             ae.append(0)
#         aw.append(ae)
#     aq.append(aw)
# print(aq)

# ar=[12, 24, 35, 70, 88, 120, 155]
# ar.pop(0)
# ar.pop(3)
# ar.pop(3)
# print(ar)

# at=[1,3,6,78,35,55]
# ay=[12,24,35,24,88,120,155]
# au=[]
# for n in range(len(at)):
#     for m in range(len(ay)):
#         if at[n]==ay[m]:
#             au.append(at[n])
# print(au)

# def jungbok(list):
#     n=0
#     while n<len(list):
#         m=n+1
#         while m<len(list):
#             if list[n]==list[m]:
#                 list.pop(m)
#             else:
#                 m+=1
#         n+=1
#     return list

# a=[12,24,35,24,88,120,155,88,120,155]
# print(jungbok(a))

# ai={'홍길동': '010-1111-1111', '이순신': '010-1111-2222', '강감찬': '010-1111-3333'}

# print("아래 학생들의 전화번호를 조회할 수 있습니다.")
# print("홍길동")
# print("이순신")
# print("강감찬")
# name=str(input("전화번호를 조회하고자 하는 학생의 이름을 입력하십시오."))
# print("{0}의 전화번호는 {1}입니다.".format(name, ai[name]))

# o=int(input())
# ok={}
# for i in range(o):
#     ok[i+1]=(i+1)**2
# print(ok)

# al=list(input())
# i=0
# while i < len(al):
#     if al[i] == ' ' or al[i] == '!':
#         al.pop(i)
#     else:
#         i+=1
# i=0
# digit=0
# letter=0
# up=0
# low=0
# while i < len(al):
#     if al[i] == '1' or al[i] == '2' or al[i] == '3':
#         digit+=1
#     else:
#         letter+=1
#     if al[i].upper()==al[i]:
#         up+=1
#     elif al[i].lower()==al[i]:
#         low+=1
#     i+=1
# up-=digit
# print(digit,letter,up,low)

sg=list(input())
i=0
acount, bcount, ccount, dcount, ecount, fcount, gcount = 0, 0, 0, 0, 0, 0, 0
while i<len(sg):
    if sg[i]=='a':
        acount+=1
    elif sg[i]=='b':
        bcount+=1
    elif sg[i]=='c':
        ccount+=1
    elif sg[i]=='d':
        dcount+=1
    elif sg[i]=='e':
        ecount+=1
    elif sg[i]=='f':
        fcount+=1
    else:
        gcount+=1
    i+=1
print(acount,bcount,ccount,dcount,ecount,fcount,gcount)