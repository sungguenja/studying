a=int(input("what do you want to factorizate? : "))
n=1
x=0

while n<=a:
    b=a%n
    if b==0:
        print("{0} is {1}'s prime".format(n,a))
        x += 1
    n += 1

if x==2:
        print("{0} is prime number".format(a))