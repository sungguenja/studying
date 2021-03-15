import sys
INF = sys.maxsize
# 현재 트리에 인접한 정점들 중에서 가장 가까운 정점을 찾는 함수
def getMinVertex(dist,selected):
    minv = 0
    mindist = INF
    for v in range(len(dist)):
        if not selected[v] and mindist > dist[v]:
            mindist = dist[v]
            minv = v
    print(mindist,minv,vertex[minv],dist)
    return minv

def MSTPrim(vertex,adj):
    vsize = len(vertex)
    dist = [INF]*vsize
    selected = [False]*vsize
    dist[0] = 0 # dist[시작점], 이경우는 시작점이 0 인 케이스

    for i in range(vsize):
        u = getMinVertex(dist,selected)
        selected[u] = True
        for v in range(vsize):
            if adj[u][v] != None:
                if selected[v] == False and adj[u][v]<dist[v]:
                    dist[v] = adj[u][v]
    print(dist)

vertex = ['A','B','C','D','E','F','G']
weight = [[None] * 7 for i in range(7)]
weight[0][1] = 29
weight[0][5] = 10
weight[1][0] = 29
weight[1][2] = 16
weight[1][6] = 15
weight[2][1] = 16
weight[2][3] = 12
weight[3][2] = 12
weight[3][4] = 22
weight[3][6] = 18
weight[4][3] = 22
weight[4][5] = 27
weight[4][6] = 25
weight[5][0] = 10
weight[5][4] = 27
weight[6][1] = 15
weight[6][3] = 18
weight[6][4] = 25
MSTPrim(vertex,weight)