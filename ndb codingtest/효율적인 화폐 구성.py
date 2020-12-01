N,M = map(int,input().split())
money = [-1]*N
for i in range(N):
    money[i] = int(input())
case = [100000]*(M+1)
case[0] = 0
for i in range(N):
    n=money[i]
    for j in range(n,M+1):
        if case[j-n] == 100000:
            if j%n==0:
                case[j] = j//n
        else:
            case[j] = min(case[j-n]+1,case[j])
        print(case)
print(case)