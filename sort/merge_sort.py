def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    print(left,right)
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge(sorted_left,sorted_right)

def merge(left, right):
    i=0
    j=0
    result = []
    print(left,right,'in merge')
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
    while i<len(left):
        result.append(left[i])
        i += 1
    while j<len(right):
        result.append(right[j])
        j += 1
    print(result)
    return result

array = [7,5,9,0,3,1,6,2,4,8]
print(merge_sort(array))