def find(n):
    global result
    no_freind = -1
    for i in range(n):
        if not visit[i]:
            no_freind = i
            break
    
    if no_freind == -1:
        result += 1

    for j in range(no_freind+1,n):
        if not visit[j] and freind[no_freind][j]:
            visit[i]=True
            visit[j]=True
            find(n)
            visit[i]=False
            visit[j]=False


for t in range(1,int(input())+1):
    N,M=map(int,input().split())
    visit = [False]*N
    are_freind = list(map(int,input().split()))
    freind = [[False]*N for _ in range(N)]
    result = 0
    for i in range(M):
        freind[are_freind[2*i]][are_freind[2*i+1]] = True
        freind[are_freind[2*i+1]][are_freind[2*i]] = True
    find(N)
    print(result)