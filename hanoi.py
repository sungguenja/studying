case = 0
def hano(amount,start,end):
    global case
    if amount == 1: # 실제로 이동 시키겠습니다
        case += 1
        print(start,end)
        return
    
    hano(amount-1,start,6-start-end) # n-1개를 시작 지점에서 잉여지점으로 옮기기
    hano(1,start,end)                # 마지막 바닥에 있는 것을 도착지점에 옮기기
    hano(amount-1,6-start-end,end)   # 잉여지점에서 도착점으로 n-1개 옮기기

i = int(input("몇층을 옮기고 싶으신가요?"))

print("하노이 {0}단계".format(i))
hano(i,1,2)
print("최종 행동 횟수: {0}".format(case))
