#DFS Without recurssion
def dfs_iterative(graph,start):
    visited = set()
    stack = [start]
    while stack:
        node  = stack.pop()
        if node not in visited:
            print(node)
            visited.add(node)
            stack.extend(reversed(graph[node]))
graph = {
    'A':['B','C'],
    'B':['D'],
    'C':['E'],
    'D':[],
    'E':[]
}         
dfs_iterative(graph,'A')   
