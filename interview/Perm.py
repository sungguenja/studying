def perm(visit,arr,now=[]):
    if False not in visit:
        print(now)
        return
    
    for i in range(len(arr)):
        if not visit[i]:
            visit[i] = True
            perm(visit,arr,now+[arr[i]])
            visit[i] = False

perm([False,False,False],[1,2,3])