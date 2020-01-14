def sq(x):
    return x**2

a=int(input("we can find squre num from 1 to what u input"))
print(list(map(sq, range(1,a+1))))

