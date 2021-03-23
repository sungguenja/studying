arr = [True]*1001
arr[0] = False
arr[1] = False

i = 2
while i**2<=1000:
    j = i*i
    while j <= 1000:
        arr[j] = False
        j += i
    i += 1

for i in range(1001):
    if arr[i]:
        print(i, end=" ")