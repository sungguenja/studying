array = [7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)-1):
    j = array.index(min(array[i:]))
    array[i],array[j]=array[j],array[i]
print(array)