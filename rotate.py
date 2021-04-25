def rotate(arr):
    N = len(arr)
    rot = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            rot[j][N-1-i] = arr[i][j]
    return rot

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))