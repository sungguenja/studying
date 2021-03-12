array = list(map(int,input().split()))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1,0,-1):
        isChanged = False
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                isChanged = True
        if not isChanged:
            break
    
    return arr

print(bubble_sort(array))