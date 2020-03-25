direction = [
    [[0,0],[1,0],[0,1]],
    [[0,0],[0,1],[1,1]],
    [[0,0],[1,0],[1,1]],
    [[0,0],[1,0],[1,-1]]
    ]

def game(board,i,j,case,delta):
    ok = True
    for k in range(3):
        ni = i+direction[k][i][0]
        nj = j+direction[k][i][1]
        if ni<0 or ni>=len(board) or nj<0 or nj>=len(board[ni]):
            ok = False
        elif board[ni][nj] + delta > 1:
            ok = False
    return ok

def cover(board):
    y,x=-1,-1
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                y=i
                x=j
                break
        if y == -1:
            break
    
    if y==-1:
        return 1

    ret=0
    for t in range(4):
        if game(board,y,x,t,-1):
            ret+=cover(board)
        game(board,y,x,t,-1)
    return ret