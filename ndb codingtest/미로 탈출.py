from collections import deque
N,M = map(int,input().split())
maze = [list(input()) for i in range(N)]
visit = [[0]*M for i in range(N)]
di = [0,1,0,-1]
dj = [1,0,-1,0]
Que = deque()
Que.append([0,0,1])
while len(Que) != 0:
    i,j,cnt = Que.popleft()
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<N and 0<=nj<M and maze[ni][nj] == '1' and (visit[ni][nj] == 0 or visit[ni][nj]>cnt+1):
            visit[ni][nj] = cnt + 1
            Que.append([ni,nj,cnt+1])
print(visit[-1][-1])