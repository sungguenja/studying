def fibo_recursion(n):        #recursion method is calling itself again and again
    if n<2:
        return n
    else:
        return fibo_recursion(n-1)+fibo_recursion(n-2)

def fibo_memo(n):           # memoization save glo
    global memo
    if n>=2 and len(memo)<=n:
        memo.append(fibo_memo(n-1)+fibo_memo(n-2))
    return memo[n]

def fibo_dp(n):
    dp = [0,1]
    for z in range(2,n+1):
        dp.append(dp[z-1]+dp[z-2])
    return dp[n]


memo = [0,1]
for i in range(1,11):
    print(fibo_recursion(i), end=' ')
print()

for i in range(11,21):
    print(fibo_memo(i), end=' ')
print()

for i in range(21,31):
    print(fibo_dp(i), end=' ')
