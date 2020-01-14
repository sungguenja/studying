def even(x):
    if x%2==0:
        return x

a=int(input("we can find even num from 0 to what u input:"))
print(list(filter(even, range(1,a))))