array = [7,5,9,0,3,1,6,2,4,8]
def quick_sort(arr,start,end):
    if start>=end:
        return
    pivot = start
    left = start+1
    right = end
    while left<=right:
        print(arr,arr[pivot],pivot,arr[left],left,arr[right],right)
        while left<=end and arr[left] <= arr[pivot]:
            left += 1
        while right>start and arr[right] >= arr[pivot]:
            right -= 1
        if left <= right:
            arr[left],arr[right] = arr[right],arr[left]
        else:
            arr[right],arr[pivot] = arr[pivot],arr[right]
    quick_sort(arr,start,right-1)
    quick_sort(arr,right+1,end)
quick_sort(array,0,len(array)-1)