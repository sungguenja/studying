from copy import deepcopy
import sys
INF = sys.maxsize
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

def floyd():
    vsize = len(vertex)
    A = deepcopy(weight)
    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                A[i][j] = min(A[i][j],A[i][k]+A[k][j])
    
    for fl in A:
        print(fl)

floyd()