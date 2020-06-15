direction = [
    [[0,0],[0,1],[1,0]],
    [[0,0],[0,1],[1,1]],
    [[0,0],[1,0],[1,1]],
    [[0,0],[1,0],[1,-1]]
]
def sticker(N,M,cnt):
    global answer
    if cnt == 0:
        answer += 1
        return
    trigger = False
    for i in range(N):
        for j in range(M):
            if game[i][j] == '.':
                trigger = True
                for k in direction:
                    for shape in k:
                        ni = i+shape[0]
                        nj = j+shape[1]
                        if 0>ni or ni>=N or 0>nj or nj>=M or game[ni][nj]=='#':
                            break
                    else:
                        for shape in k:
                            ni = i+shape[0]
                            nj = j+shape[1]
                            game[ni][nj] = '#'
                        sticker(N,M,cnt-3)
                        for shape in k:
                            ni = i+shape[0]
                            nj = j+shape[1]
                            game[ni][nj] = '.'
                break
        if trigger:
            break

for t in range(1,int(input())+1):
    N,M = map(int,input().split())
    dot = 0
    game = [0]*N
    for i in range(N):
        game[i] = list(input())
        dot += game[i].count('.')
    answer = 0
    if dot%3 != 0:
        print(answer)
    else:
        sticker(N,M,dot)
        print(answer)