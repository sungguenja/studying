# 탐색 값과 위치는 비례한다는 가정이 있어야한다.
def interpolation_search(array,key,low,high):
    if low<=high:
        middle = int(low + (high-low)*(key-array[low])/(array[high]-array[low]))
        if key == array[middle]:
            return middle
        elif key < array[middle]:
            return interpolation_search(array,key,low,middle-1)
        else:
            return interpolation_search(array,key,middle+1,high)
    return None

arr = [1,3,7,9,10,12,16,18,40]
print(interpolation_search(arr,7,0,len(arr)-1))