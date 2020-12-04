import heapq
INF = int(1e9)
N,M = map(int,input().split())
start = int(input())
graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)
visited = [False]*(N+1)
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist,now = heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))