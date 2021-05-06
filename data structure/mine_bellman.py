import sys
INF = sys.maxsize
def bellman_ford(graph,start):
    distance = {}
    predecessor = {}
    
    # 거리 값, 이전 정점 초기화
    for node in graph:
        distance[node] = INF
        predecessor[node] = None
    distance[start] = 0

    # V-1개마큼 반복
    for _ in range(len(graph)-1):
        for node in graph:
            for neigbor in graph[node]:
                if distance[neigbor] > distance[node] + graph[node][neigbor]:
                    distance[neigbor] = distance[node] + graph[node][neigbor]
                    predecessor[neigbor] = node
    
    # 음수 사이클이 존재하는지 (1번더 반복후 V-1번 반복했을때랑 같으면 음수사이클X 다르면 음수사이클 존재)
    for node in graph:
        for neigbor in graph[node]:
            if distance[neigbor] > distance[node] + graph[node][neigbor]:
                return -1, "그래프에 음수 사이클이 존재합니다."
    
    return distance,graph

# 음수 사이클이 존재하지 않는 그래프
graph = {
    'A': {'B': -1, 'C':  4},
    'B': {'C':  3, 'D':  2, 'E':  2},
    'C': {},
    'D': {'B':  1, 'C':  5},
    'E': {'D': -3}
}

# 그래프 정보와 시작 정점을 넘김
distance, predecessor = bellman_ford(graph, start='A')

print(distance)
print(predecessor)


# 음수 사이클이 존재하는 그래프
graph = {
    'A': {'B': -1, 'C':  4},
    'B': {'C':  3, 'D':  2, 'E':  2},
    'C': {'A': -5},
    'D': {'B':  1, 'C':  5},
    'E': {'D': -3}
}


distance, predecessor = bellman_ford(graph, start='A')

print(distance)
print(predecessor)