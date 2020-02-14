def per_rep(num_list=[]):

    if visit==visited:
        root.append(num_list)

    for i in range(4):
        if visit[i] != visited[i]:
            visit[i] += 1
            per_rep(num_list+[A[i]])
            visit[i] -= 1



A=[1,2,3,4]
visit = [0,0,0,0]
visited = [2,3,0,1]
root = []
per_rep()
print(root)