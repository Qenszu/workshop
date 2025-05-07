#3. Dobry początek: G -> skierowany, czy dojde do kazdego 

def dfs(G, start_vertex):
    # Mark all vertices as not visited
    visited = [False] * len(G) 
        
        
    # Call the recursive helper function
    _dfs_recursive(G, start_vertex, visited)
        
    return visited
    
def _dfs_recursive(G, vertex, visited):
    # Mark the current node as visited and add to traversal
    visited[vertex] = True
        
    # Recur for all adjacent vertices
    for neighbor in G[vertex]:
        if not visited[neighbor]:
            _dfs_recursive(G, neighbor, visited)


G = [
    [1, 2],
    [2, 3],
    [5],
    [4],
    [6],
    [],
    []
]

def xd(G, v):
    t = dfs(G, v)
    for i in range(len(G)):
        if not t[i]:
            return False
        return True
print(xd(G, 0))