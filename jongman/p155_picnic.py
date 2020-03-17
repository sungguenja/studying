def countpairings(n):
    first_free = -1
    for i in range(n):
        if not taken[i]:
            first_free = i
            break
    
    if first_free == -1:
        return 1
    
    ret = 0
    for i in range(first_free+1,n):
        if not taken[i] and are_friends[first_free][i]:
            taken[first_free] = True
            taken[i] = True
            ret += countpairings(n)
            taken[first_free] = False
            taken[i] = False
    
    return ret

for t in range(int(input())):
    N,M = map(int,input().split())
    friend_list = list(map(int,input().split()))
    are_friends = [[False]*N for _ in range(N)]
    for i in range(M):
        are_friends[friend_list[i*2]][friend_list[i*2+1]] = True
        are_friends[friend_list[i*2+1]][friend_list[i*2]] = True
    taken=[False]*N
    cnt = countpairings(N)
    print(cnt)
    