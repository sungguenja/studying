array = list(map(int,input().split()))

def sellection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        minimum = arr[i]
        minimum_position = i
        for j in range(i+1,n):
            if arr[j]<minimum:
                minimum = arr[j]
                minimum_position = j
        arr[i],arr[minimum_position] = arr[minimum_position],arr[i]
    return arr

print(sellection_sort(array))