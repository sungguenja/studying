array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
check = [0]*(max(array)+1)
for i in range(len(array)):
    check[array[i]] += 1
sorted_array = []
for i in range(len(check)):
    if check[i] != 0:
        for j in range(check[i]):
            sorted_array.append(i)
print(sorted_array)