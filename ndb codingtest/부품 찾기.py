N = int(input())
ndb = list(map(int,input().split()))
M = int(input())
customer = list(map(int,input().split()))
ndb.sort()
answer = ['no']*M
def solution(left,right,check,whe):
    mid = (left+right)//2
    if ndb[mid] == check:
        answer[whe] = 'yes'
    elif ndb[mid] > check:
        if right != mid:
            solution(left,mid,check,whe)
    else:
        if left != mid:
            solution(mid,right,check,whe)
for i in range(M):
    solution(0,N,customer[i],i)
print(' '.join(answer))