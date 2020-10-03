N,M,K = map(int,input().split())
numbers = list(map(int,input().split()))

numbers.sort()
answer = 0
best = numbers[-1]
nobest = numbers[-2]
answer = 0
while True:
    for i in range(K):
        if M == 0:
            break
        answer += best
        M -= 1
    if M == 0:
        break
    answer += nobest
    M -= 1

print(answer)