array = list(map(int,input().split()))

def merge_sort(array):
    if len(array) == 1:
        return array
    
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    divided_left = merge_sort(left)
    divided_right = merge_sort(right)

    return merge(divided_left,divided_right)

def merge(left,right):
    n = len(left)+len(right)
    sorted_array = [0]*n
    cnt = 0
    print(left,right)
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorted_array[cnt] = left[i]
            i += 1
        else:
            sorted_array[cnt] = right[j]
            j += 1
        cnt += 1
    
    while i<len(left):
        sorted_array[cnt] = left[i]
        i += 1
        cnt += 1
    
    while j<len(right):
        sorted_array[cnt] = right[j]
        j += 1
        cnt += 1
    
    return sorted_array

print(merge_sort(array))