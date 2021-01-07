arr = [41,34,6,16,38,36,28,19,43,59,45]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
            print(arr,i,j)