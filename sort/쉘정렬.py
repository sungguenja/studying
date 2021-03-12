def shell_sort(a):
    h = 4
    while h >= 1:
        for i in range(h,len(a)):
            j = i
            while j >= h and a[j] < a[j-h]:
                a[j],a[j-h] = a[j-h],a[j]
                j -= h
        h //= 3
        print(a)
    return a

a = [54,88,77,26,93,17,49,10,17,77,11,31,22,44,17,20]
print(a)
print(shell_sort(a))