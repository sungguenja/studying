parent = []
set_size = 0
def init_set(nSets):
    global set_size,parent
    set_size = nSets
    for i in range(nSets):
        parent.append(-1)

def find(id):
    while parent[id] >= 0:
        id = parent[id]
    return id

def union(s1,s2):
    global set_size
    parent[s1] = s2
    set_size -= 1
    