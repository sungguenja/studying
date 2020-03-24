def prim(G,s,N):
    key = [99999]*N
    visit = [False]*N
    pi = [None]*N
    key[s] = 0

    for _ in range(N):
        min_num = 9999999
        minindex = -1
        for i in range(N):
            if not visit[i] and key[i]<min_num:
                min_num = key[i]
                minindex = i
        
        visit[minindex] = True
        for v,val in G[minindex]:
            if not visit[v] and val<key[v]:
                key[v]=val
                pi[v]=minindex
    
    return key

def dijkstra(G,s,N):
    D = [99999]*N
    P = [None]*N
    visit = [False]*N
    D[s] = 0

    for _ in range(N):
        min_num=99999
        minindex=-1
        for i in range(N):
            if not visit[i] and D[i] < min_num:
                min_num=D[i]
                minindex = i
        visit[minindex] = True
        for v, val in G[minindex]:
            if not visit[v] and D[minindex]+val<D[v]:
                D[v] = D[minindex]+val
                P[v] = minindex
    
    return D
