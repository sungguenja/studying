def fastSum(n):
    if n==1:
        return n
    elif n%2==1:
        return fastSum(n-1) + n
    else:
        return 2*fastSum(n//2)+(n//2)*(n//2)
print(fastSum(10))