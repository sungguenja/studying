def chess(n,start=None,visit=[]):
    if start != None:
        visit = visit + [start]
    
    if len(visit) == n:
        memo.append(visit)

    for i in range(n):
        if i not in visit:
            if visit == []:
                chess(n,i,visit)
            else:
                for j in range(-1,-1*len(visit)-1,-1):
                    if i == visit[j] + j or i == visit[j] - j:
                        break
                else:
                    chess(n,i,visit)
for i in range(1,9):
    memo = []
    chess(i)
    print(len(memo))