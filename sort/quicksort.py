def quicksort(arr,start,end):
    if start>=end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        print(arr,arr[pivot])
        while left <= end and arr[pivot] >= arr[left]:
            left += 1
        while start < right and arr[pivot] <= arr[right]:
            right -= 1
        if 0<=left<len(arr) and 0<=right<len(arr):
            print(arr,left,right,arr[left],arr[right],arr[pivot])
        else:
            print(arr,left,right)
        if left < right:
            arr[left],arr[right] = arr[right],arr[left]
        else:
            arr[right],arr[pivot] = arr[pivot],arr[right]
        print(arr)
    quicksort(arr,start,right)
    quicksort(arr,right+1,end)
array = [7,5,9,0,3,1,6,2,4,8]
quicksort(array,0,len(array)-1)