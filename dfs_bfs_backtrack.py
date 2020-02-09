# def dfs(graph,root):
#     visited = []
#     stack = [root]

#     while stack:
#         vertax = stack.pop()
#         if vertax not in visited:
#             visited.append(vertax)
#             stack.extend(graph[vertax]-visited)
        
#     return visited


root = {'A':['B','C','E'],'B':['A','D','F'],'C':['A','G'],'D':['B'],'E':['A','F'],'F':['B','E'],'G':['C']}

paths = []

def dfs_paths(graph, start, end, visited=[]):
    visited = visited + [start]

    if start == end:
        paths.append(visited)
    
    for node in graph[start]:
        if node not in visited:
            dfs_paths(graph, node, end, visited)

dfs_paths(root, 'A', 'F')
print(paths)