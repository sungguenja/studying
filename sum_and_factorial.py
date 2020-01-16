def plus(): # 합계산기
    print("how many do u want to sum from 1")
    n = 1
    s = 0
    a = int(input())

    if a < 0:
        print("that is minus")
    else:
        while n < a + 1:
            s = s + n
            n = n + 1
        print(s, "is this?")


def fac(): # 펙토리얼계산
    print("what do u find factorial?")
    n = 1
    s = 1
    a = int(input())

    if a < 0:
        print("i think that is not positive num")
    else:
        while n < a + 1:
            s = s * n
            n = n + 1
        print(s, "take this")


def start():
    print("pls input num that u want to start program? sum:1 factorial:2 turn off:3")
    x = int(input())
    if x == 1:
        plus()
        start()
    else:
        if x == 2:
            fac()
            start()
        else:
            print("naniiiiiiiiiiii")


start()