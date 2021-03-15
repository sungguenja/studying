import mine_union_find
def Kruskal(vertex,adj): # vertext는 정점 리스트, adj는 인접행렬
    vsize = len(vertex)
    mine_union_find.init_set(vertex)
    eList = []

    for i in range(vsize-1):
        for j in range(i+1,vsize):
            if adj[i][j] != None:
                eList.append((i,j,adj[i][j]))

    # 가중치 순으로 정렬 시키자
    eList.sort(key = lambda e: e[2], reverse = True)

    edgeAccepted = 0
    while edgeAccepted < vsize - 1: # 간선의 선택수는 노드-1개이다
        selected_line = eList.pop(-1)
        uset = mine_union_find.find(selected_line[0])
        vset = mine_union_find.find(selected_line[1])

        if uset != vset:
            edgeAccepted += 1
            mine_union_find.union(uset,vset)
            print("추가된 간선 : ",vertex[selected_line[0]],vertex[selected_line[1]],selected_line[2])