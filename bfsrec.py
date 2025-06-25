#bfs recursive method
'''
def bfs_recursive(graph,start):
    visited = set()
    queue = [start]
    while queue:
        node  = queue.pop(0)
        if node not  in visited:
            print(node)
            visited.add(node)
            queue.extend(graph[node])
graph = {
    'A':['B','C'],
    'B':['D'],
    'C':['E'],
    'D':[],
    'E':[]
}         
print(bfs_recursive(graph,'A'))            
'''
def bfs_recursive(graph, queue=None, visited=None):
    if queue is None:
        queue = []
    if visited is None:
        visited = set()
    if not queue:
        return
    node = queue.pop(0)
    if node not in visited:
        print(node)
        visited.add(node)
        queue.extend([n for n in graph[node] if n not in visited])
    bfs_recursive(graph, queue, visited)
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],  
    'D': [],
    'E': []
}
bfs_recursive(graph, queue=['A'])