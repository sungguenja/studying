can_i = [0,1,1,1,0,-1,-1,-1]
can_j = [1,1,0,-1,-1,-1,0,1]

def word(i,j,fword,visit,num=1):
    if num==len(fword):
        answer.append(visit)
        return
    
    for k in range(8):
        ni = i+can_i[k]
        nj = j+can_j[k]
        if 0<=ni<5 and 0<=nj<5:
            if game[ni][nj] == fword[num]:
                word(ni,nj,fword,visit+[[ni,nj]],num+1)

game = [
    ['U','R','L','P','M'],
    ['X','P','R','E','T'],
    ['G','I','A','E','T'],
    ['X','T','N','Z','Y'],
    ['X','O','Q','R','S']
]

answer = []
want_word = str(input('찾을 단어를 입력하시오 : '))
for i in range(5):
    for j in range(5):
        if game[i][j] == want_word[0]:
            word(i,j,want_word,[[i,j]])

for k in answer:
    print(k)