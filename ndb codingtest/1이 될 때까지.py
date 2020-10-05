N,M = map(int,input().split())
answer = 0
while N>1:
    if N%M == 0:
        N = N//M
        answer += 1
    else:
        while N%M != 0:
            N-=1
            answer += 1
            if N==1:
                break
print(answer)