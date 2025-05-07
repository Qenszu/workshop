from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def shortest_path_bfs(self, start_vertex, end_vertex):
        # Mark all vertices as not visited
        visited = [False] * self.vertices
        
        # Create a queue for BFS
        queue = deque()
        
        # Store predecessors of each vertex to reconstruct the path
        predecessor = [-1] * self.vertices
        
        # Mark the start vertex as visited and enqueue it
        visited[start_vertex] = True
        queue.append(start_vertex)
        
        # BFS loop
        while queue and not visited[end_vertex]:
            # Dequeue a vertex from queue
            current = queue.popleft()
            
            # Visit all adjacent vertices
            for neighbor in self.graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    predecessor[neighbor] = current
        
        # If end_vertex was never visited, no path exists
        if not visited[end_vertex]:
            return []
        
        # Reconstruct the path from end_vertex to start_vertex
        path = []
        current = end_vertex
        print(predecessor)
        while current != -1:
            path.append(current)
            current = predecessor[current]
        
        # Reverse to get path from start to end
        return path[::-1]

# Example usage
g = Graph(6)

# Add edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 5)
g.add_edge(1, 5)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

# Find shortest path from vertex 0 to vertex 5
path = g.shortest_path_bfs(0, 5)
if path:
    print(f"Shortest path from 0 to 5: {' -> '.join(map(str, path))}")
else:
    print("No path exists between 0 and 5")