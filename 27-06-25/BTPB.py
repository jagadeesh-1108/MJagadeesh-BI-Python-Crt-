''' Vignan campus Map
Each building in a college campus is a node, and walkable paths are edges.
Represent the campus map using an adjacency list.
Check if there's a path from the library to the auditorium using BFS.
List all buildings that are directly connected to the Admin Block.
Use DFS to visit all reachable buildings from the Main Gate.
Find if there are any disconnected buildiings (buildings not connected to campus).'''
campus={
    "Main Gate":["Admin Block"],
    "Admin Block":["Main Gate","Library","Canteen","Engineering Block"],
    "Library":["Admin Block","Auditorium"],
    "Canteen":["Admin Block","Hostel"],
    "Auditorium":["Library"],
    "Engineering Block":["Admin Block","Science Block"],
    "Science Block":["Engineering Block"],
    "Hostel":["Canteen"]
}
def bfs(start,target):
    visited=set()
    queue=[start]
    while queue:
        b=queue.pop(0)
        if b==target:
            return True
        if b not in visited:
            visited.add(b)
            queue+=[n for n in campus[b] if n not in visited]
    return False
def dfs(start,visited=None):
    if visited is None:
        visited=set()
    if start in visited:
        return
    print(start,end=' ')
    visited.add(start)
    for neighbor in campus[start]:
        dfs(neighbor,visited)
def disconnected():
    visited=set()
    dfs(next(iter(campus)),visited)
    return set(campus.keys())-visited
#1.Adjacency List
print("1. Campus Map:")
for b, n in campus.items():
    print(f"{b} -> {', '.join(n)}")
#2.Path from library to auditorium
print("\n2. Path from Library to Auditorium exists:")
print("Yes" if bfs("Library", "Auditorium")else "No")
#3. Direct connection from Admin Block
print("\n3. Direct connections from Admin Block:")
print(campus["Admin Block"])
#4. DFS from Main Gate
print("\n4. DFS from Main Gate:")
dfs("Main Gate")
print()
#5. isconnected Buildings
print("\n5. Disconnected Buildings:")
d=disconnected()
print(d if d else "None, campus is fully connected")