N = int(input())
command = list(input().split())
direct = {'R':[0,1],'U':[-1,0],'L':[0,-1],'D':[1,0]}
i = 1
j = 1
for k in command:
    ni = i + direct[k][0]
    nj = j + direct[k][1]
    if 0<ni<=N and 0<nj<=N:
        i = ni
        j = nj
print(i,j)