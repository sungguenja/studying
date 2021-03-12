arr = list(map(int,input().split()))

def pancake_sort(array):
    N = len(array)
    for i in range(N,0,-1):
        print(array)
        now_max = max(array[:i])
        now_whe = array[:i].index(now_max)
        array[0],array[now_whe] = array[now_whe],array[0]
        print(array)
        print(array[:i][::-1],array[i:])
        array = array[:i][::-1] + array[i:]
    return array
print(pancake_sort(arr))