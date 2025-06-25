#BFS - Breadth first search 
def dfs_recursive(graph,node,visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph,neighbor,visited)
graph = {
    'A':['B','C'],
    'B':['D'],
    'C':['E'],
    'D':[],
    'E':[]
}         
print(dfs_recursive(graph,'A',set()))





