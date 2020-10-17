from collections import deque
N,M = map(int,input().split())
icecream_frame = [list(input()) for i in range(N)]
icecream_count = 0
di = [0,1,0,-1]
dj = [1,0,-1,0]
visit = [[0]*M for i in range(N)]
for i in range(N):
    for j in range(M):
        if icecream_frame[i][j] == '0' and visit[i][j] == 0:
            visit[i][j] = 1
            Que = deque()
            Que.append([i,j])
            icecream_count += 1
            while len(Que) != 0:
                ni,nj = Que.popleft()
                for k in range(4):
                    nni = ni + di[k]
                    nnj = nj + dj[k]
                    if 0<=nni<N and 0<=nnj<M:
                        if icecream_frame[nni][nnj] == '0' and visit[nni][nnj] == 0:
                            visit[nni][nnj] = 1
                            Que.append([nni,nnj])
print(icecream_count)