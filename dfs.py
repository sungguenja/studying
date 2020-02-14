root = {'A':['B','C','E'],'B':['A','D','F'],'C':['A','G'],'D':['B'],'E':['A','F'],'F':['B','E'],'G':['C']}

paths = []

def dfs_paths(graph, start, end, visited=[]):
    visited = visited + [start]

    if start == end:
        paths.append(visited)
        return 1
    
    for node in graph[start]:
        if node not in visited:
            dfs_paths(graph, node, end, visited)

print(dfs_paths(root, 'A', 'F'))
print(paths)
