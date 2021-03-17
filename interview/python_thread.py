from threading import Thread

def work(id,start,end,result):
    total = 0
    for i in range(start,end):
        total += i
    result.append(total)
    return

if __name__ == "__main__":
    start,end = 0,100000000
    result = list()
    th1 = Thread(target=work,args=(1,start,end//2,result))
    th2 = Thread(target=work,args=(2,end//2,end,result))
    th1.start()
    th2.start()
    th1.join()
    th2.join()