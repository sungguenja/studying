def recur(C,n):
    if n==1:
        return C
    elif n%2==0:
        y=recur(C,n//2)
        return y*y
    elif n%2==1:
        y=recur(C,(n-1)//2)
        return y*y*C

for i in range(1,11):
    print(recur(2,i))