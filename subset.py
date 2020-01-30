N=int(input())
M=int(input())
arr = list(range(N))
n=len(arr)
count = 0
for i in range(2**M -1, 2**N - 2**(M-1) + 1):
    x=[]
    C=list(bin(i)[2:])
    if C.count('1') != M:
        continue
    for j in range(n):
        if i&(1<<j):
            x.append(arr[j])
            count += 1
    print(x,C)
print(count//M)

# for i in range(n):
# print(1&10)
# def combi(n,k):
#     if k==0:
#         return 1
#     elif k==1:
#         return n
#     elif n==k:
#         return 1
#     else:
#         return combi(n-1,k)+combi(n-1,k-1)

# print(combi(10,2))
# def combo(molist,n,k):
#     buboon = []
#     if k==1:
#         for i in range(n):
#             bu