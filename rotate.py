def rotate(arr):
    N = len(arr)
    rot = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            rot[j][N-1-i] = arr[i][j]
    return rot

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
asd = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
asd = rotate(asd)
for k in asd:
    print(k)