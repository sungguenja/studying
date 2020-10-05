N,M = map(int,input().split())
answer = -1
for i in range(N):
    now_min = min(list(map(int,input().split())))
    answer = max(answer,now_min)
print(answer)