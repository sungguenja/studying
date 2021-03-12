def redix_sort(array,n):
    length = len(array)
    for i in range(n):
        queue = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
        redix_array = []
        for j in range(length):
            queue[(array[j]//(10**i))%10].append(array[j])
        for key in queue.keys():
            for value in queue[key]:
                redix_array.append(value)
        array = redix_array
        print(array)
    return array

arr = list(map(int,input().split()))
n = 0
for i in range(len(arr)):
    cnt = 0
    while True:
        if arr[i]//(10**cnt) > 0:
            cnt += 1
        else:
            break
    if cnt > n:
        n = cnt
print(n)
print(redix_sort(arr,n))