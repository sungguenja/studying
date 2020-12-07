def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return x

def union_parent(parent,x,y):
    a = find_parent(parent,x)
    b = find_parent(parent,y)
    if a>=b:
        parent[a] = b
    else:
        parent[b] = a

v,e = map(int,input().split())
parent = [i for i in range(v+1)]

for i in range(e):
    a,b=map(int,input().split())
    union_parent(parent,a,b)

# 소속 집합
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')
print()

# 부모 테이블
print(parent)