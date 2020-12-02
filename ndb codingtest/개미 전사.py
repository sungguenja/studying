N = int(input())
stock = list(map(int,input().split()))
ant = [-1]*N
ant[0] = stock[0]
ant[1] = max(stock[1],ant[0])
for i in range(2,N):
    ant[i] = max(ant[i-2]+stock[i],ant[i-1])
print(ant)