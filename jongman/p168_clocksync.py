link = [[0,1,2],[3,7,9,11],[4,10,14,15],[0,4,5,6,7],[6,7,8,10,12],[0,2,14,15],[3,14,15],[4,5,7,14,15],[1,2,3,4,5],[3,4,5,9,13]]
def clock(timer,start=0,cnt=0):
    global min_count
    if min_count!=-1 and cnt>=min_count:
        return
    elif timer == [12]*16 and (min_count==-1 or cnt<min_count):
        min_count=cnt
        return
    
    for i in range(start,10):
        if visit[i]<3:
            visit[i]+=1
            for k in link[i]:
                timer[k] += 3
                if timer[k] == 15:
                    timer[k] = 3
            clock(timer,start,cnt+1)
            for k in link[i]:
                timer[k] -= 3
                if timer[k] == 0:
                    timer[k] = 12
            visit[i]-=1

for t in range(int(input())):
    clo=list(map(int,input().split()))
    min_count = 16
    visit = [0]*10
    clock(clo)
    print(min_count)