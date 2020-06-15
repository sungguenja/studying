switch = [
    [0,1,2],
    [3,7,9,11],
    [4,10,14,15],
    [0,4,5,6,7],
    [6,7,8,10,12],
    [0,2,14,15],
    [3,14,15],
    [4,5,7,14,15],
    [1,2,3,4,5],
    [3,4,5,9,13]
]
def clock_switch(timer,time=0):
    global minimum_times
    if time>=minimum_times:
        return
    
    if timer == [12]*16:
        if time<minimum_times:
            minimum_times = time
        return
    
    for i in range(len(switch)):
        for j in switch[i]:
            timer[j] -= 3
            if timer[j] == 0:
                timer[j] = 12
        clock_switch(timer,time+1)
        for j in switch[i]:
            timer[j] += 3
            if timer[j] == 15:
                timer[j] = 3

for t in range(1,int(input())+1):
    clock = list(map(int,input().split()))
    minimum_times=9999
    clock_switch(clock)
    if minimum_times == 9999:
        minimum_times = -1
    print(minimum_times)