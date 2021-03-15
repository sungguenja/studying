from collections import deque
import sys
INF = sys.maxsize
dp = [INF]*7
vertex = ["A","B","C","D","E","F","G"]
weight = [
    [0,7,INF,INF,3,10,INF],
    [7,0,4,10,2,6,INF],
    [INF,4,0,2,INF,INF,INF],
    [INF,10,2,0,11,9,4],
    [3,2,INF,11,0,13,5],
    [10,6,INF,9,13,0,INF],
    [INF,INF,INF,4,5,INF,0]
]

def dijkstra(start):
    Que = deque()
    dp[start] = 0
    Que.append((start,0))
    while Que:
        now,cost = Que.popleft()
        for i in range(7):
            if weight[now][i] != INF:
                next_cost = cost + weight[now][i]
                if next_cost < dp[i]:
                    dp[i] = next_cost
                    Que.append((i,next_cost))

dijkstra(0)
print(dp)