def countdown(a):
    if a>0:
        while a>0:
            print(a)
            a -= 1
    else:
        print("pls input int that is bigger 0.")

x=int(input())
countdown(x)