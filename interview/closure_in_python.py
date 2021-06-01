def afunc():
    a = 0
    
    def increaseFunc():
        nonlocal a
        a += 1
    
    def decreaseFunc():
        nonlocal a
        a -= 1
    
    def printA():
        print(a)
    
    return increaseFunc,decreaseFunc,printA

aaa,bbb,ccc = afunc()
print(aaa,bbb,ccc)
aaa()
ccc()
bbb()
ccc()
bbb()
ccc()