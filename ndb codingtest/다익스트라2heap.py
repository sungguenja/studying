import heapq
INF = int(1e9)
N,M = map(int,input().split())
start = int(input())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
distance = [INF]*(N+1)
for _ in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        cost,now = heapq.heappop(q)
        if distance[now]<cost:
            continue
        for i in graph[now]:
            now_cost = cost + i[1]
            if now_cost<distance[i[0]]:
                distance[i[0]] = now_cost
                heapq.heappush(q,(now_cost,i[0]))
            print(distance)

dijkstra(start)