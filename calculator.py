def sum():
    print("pls input two number which is wanted to sum")
    a=float(input())
    b=float(input())
    a+=b
    print("if u want some more pls input 1, else pls 2")
    c=int(input())
    while c==1:
        print("input number")
        b=float(input())
        a+=b
        print("want some more? press 1, nope? press 2")
        c=int(input())
    print("this is result",a)

def minus():
    print("pls input two number. that number will be used to minus")
    a = float(input())
    b = float(input())
    a -= b
    print("want more? press 1, if u don't? press 2")
    c = int(input())
    while c == 1:
        print("more number")
        b = float(input())
        a -= b
        print("if u want to minus more, press 1, else 2")
        c = int(input())
    print("this is result", a)

def mult():
    print("press number to multiplicate")
    a = float(input())
    b = float(input())
    a *= b
    print("if u want to more multiple, code 1, nope? code 2")
    c = int(input())
    while c == 1:
        print("input number")
        b = float(input())
        a *= b
        print("if u want to more multiple, code 1, nope? code 2")
        c = int(input())
    print("result", a)

def nanugi():
    print("press two number. first number will be devided by the next")
    a = float(input())
    b = float(input())
    a = a/b
    print("want more devision? press 1, if u hate that game press 2")
    c = int(input())
    while c == 1:
        print("input number")
        b = float(input())
        a -= b
        print("more => 1, no => 2")
        c = int(input())
    print("do u want this?", a)

def cal():
    print("add:1, subtraction:2, multiplication:3, division:4, turn off:5")
    x=int(input())
    if x==1:
        sum()
        cal()
    else:
        if x==2:
            min()
            cal()
        if x==3:
            mult()
            cal()
        if x==4:
            nanugi()
            cal()
        print("this program wa mo sindeiru \n naniiiiiii?")

cal()