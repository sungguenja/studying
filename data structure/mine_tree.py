import mine_node
from collections import deque
def preorder(n):
    if n is not None:
        print(n.data)
        preorder(n.left)
        preorder(n.right)

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data)
        inorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data)

def levelorder(n):
    Que = deque()
    Que.append(n)
    while Que:
        node = Que.popleft()
        if node is not None:
            print(node.data)
            Que.append(node.left)
            Que.append(node.right)

# 최소 공통 조상 찾기
checked = [False]*21
depth = [0]*21
atree = [
    [1,2],
    [3,4],
    [5,6],
    [7,8],
    [9,10,11],
    [],
    [],
    [],
    [12,13],
    [14],
    [15],
    [],
    [],
    [16,17],
    [18],
    [19],
    [],
    [20],
    [],
    [],
    []
]
parent = [[] for i in range(21)]
log = 11
def dfs(x,dep):
    checked[x] = True
    depth[x] = dep
    for i in atree[x]:
        if checked[i]:
            continue
        parent[i].append(x)
        dfs(i,dep+1)

def setParent():
    dfs(0,0)
    for i in range(20,-1,-1):
        j = parent[i]
        while len(j) > 0:
            j = parent[j[0]]
            if len(j) == 0:
                break
            parent[i].append(j[0])

setParent()

def setSameDepth(A,B):
    while depth[A] > depth[B]:
        A = parent[A][0]
    while depth[A] < depth[B]:
        B = parent[B][0]
    
    return A,B

def findSameParent(A,B):
    value1,value2 = setSameDepth(A,B)
    while value1 != value2:
        value1 = parent[value1][0]
        value2 = parent[value2][0]
    return value1

print(findSameParent(20,15))