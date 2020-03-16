def perm(N,K,other_K,start=0,visit=[]):
    if N<=K or K==0:
        return 1
    
    if other_K == 0:
        total.append(visit)
        return
    
    for i in range(start+1,N+1):
        perm(N,K,other_K-1,i,visit+[i])

total = []
perm(7,4,4)
print(total)
print(len(total))