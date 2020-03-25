direction = [[[0,1],[1,1]],[[0,1],[-1,1]],[[1,0],[1,1]],[[1,0],[1,-1]],[[0,-1],[-1,-1]],[[0,-1],[1,-1]],[[-1,0],[-1,-1]],[[-1,0],[-1,1]]]

def boardcover(match,X,Y):
    global case
    if visit == [[1]*X]*Y :
        case += 1
        return
    
    for i in range(Y):
        for j in range(X):
            if match[i][j] == '.' and visit[i][j] == 0:
                for k in direction:
                    now = []
                    for kc in k:
                        ni=i+kc[0]
                        nj=j+kc[1]
                        if 0<=ni<Y and 0<=nj<X and match[ni][nj] == '.' and visit[ni][nj] == 0:
                            now.append([ni,nj])
                        else:
                            now.clear()
                            break
                    else:
                        for t in now:
                            ni=i+t[0]
                            nj=j+t[1]
                            visit[ni][nj] = 1
                        boardcover(match,X,Y)
                        for t in now:
                            ni=i+t[0]
                            nj=j+t[1]
                            visit[ni][nj] = 0

for t in range(int(input())):
    N,M=map(int,input().split())
    game = [0]*N
    for i in range(N):
        game[i]=list(input())
    visit =[[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if game[i][j] == '#':
                visit[i][j] = 1
    case = 0
    boardcover(game,M,N)
    print(case)