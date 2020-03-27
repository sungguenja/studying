can_i = [0,1,1,1,0,-1,-1,-1]
can_j = [1,1,0,-1,-1,-1,0,1]

def word(i,j,fword,visit,num=1):
    global answer
    if num==len(fword):
        for i in range(len(visit)):
            answer += str(game[visit[i][0]][visit[i][1]])
        answer += ' '+'YES'
        return True
    
    for k in range(8):
        ni = i+can_i[k]
        nj = j+can_j[k]
        if 0<=ni<5 and 0<=nj<5:
            if game[ni][nj] == fword[num]:
                if word(ni,nj,fword,visit+[[ni,nj]],num+1):
                    return True

for t in range(int(input())):
    game = [0]*5
    for i in range(5):
        horizon = []
        horizon = list(input())
        game[i] = horizon[:]
    for _ in range(int(input())):    
        answer = ''
        want_word = str(input())
        for i in range(5):
            trigger=False
            for j in range(5):
                if game[i][j] == want_word[0]:
                    if word(i,j,want_word,[[i,j]])==None:
                        answer=want_word+' NO'
                    else:
                        trigger=True
                        answer = want_word+' YES'
                        break
            if trigger:
                break
        if trigger:
            print(answer)
        else:
            print(want_word,'NO')