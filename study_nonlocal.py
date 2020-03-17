def asdf():
    cnt = 0
    def plus():
        nonlocal cnt
        cnt+=1
        return cnt
    return plus

a = asdf()
print(a())
print(a())
print(a())
b = asdf()
print(b())

def maker(correctlist):
    rtn = []
    for i in range(5):
        question = '문제' + str(i+1) + '의 정답 : '
        rtn.append(question+str(correctlist[i]))
    return rtn

def printcorrect():
    temp = maker([3,1,3,4,2])
    for i in range(5):
        print(temp[i])

printcorrect()