from zad1testy import runtests
from collections import deque

def keep_distance(M, x, y, d):
    n = len(M)
    
    # Funkcja pomocnicza do obliczania najkrótszej odległości między wierzchołkami
    def shortest_path(u, v):
        # Implementacja Dijkstry dla pojedynczego zapytania
        dist = [float('inf')] * n
        dist[u] = 0
        visited = set()
        
        while True:
            # Znajdź nieodwiedzony wierzchołek o najmniejszej odległości
            current = -1
            min_dist = float('inf')
            for i in range(n):
                if i not in visited and dist[i] < min_dist:
                    min_dist = dist[i]
                    current = i
            
            if current == -1 or current == v:
                break
                
            visited.add(current)
            
            # Aktualizuj odległości do sąsiadów
            for neighbor in range(n):
                if M[current][neighbor] > 0:
                    new_dist = dist[current] + M[current][neighbor]
                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist
        
        return dist[v] if dist[v] != float('inf') else -1
    
    # Sprawdzenie czy początkowa pozycja spełnia warunek
    if shortest_path(x, y) < d:
        return None
    
    # BFS w grafie stanów
    visited = {}
    parent = {}
    queue = deque()
    
    start_state = (x, y)
    queue.append(start_state)
    visited[start_state] = True
    parent[start_state] = None
    
    found = False
    end_state = (y, x)
    
    while queue:
        current = queue.popleft()
        u, v = current
        
        if current == end_state:
            found = True
            break
        
        # Generuj możliwe ruchy
        # 1. Carol się porusza, Max stoi
        for neighbor in range(n):
            if M[u][neighbor] > 0:
                new_state = (neighbor, v)
                if new_state not in visited and shortest_path(neighbor, v) >= d:
                    visited[new_state] = True
                    parent[new_state] = current
                    queue.append(new_state)
        
        # 2. Max się porusza, Carol stoi
        for neighbor in range(n):
            if M[v][neighbor] > 0:
                new_state = (u, neighbor)
                if new_state not in visited and shortest_path(u, neighbor) >= d:
                    visited[new_state] = True
                    parent[new_state] = current
                    queue.append(new_state)
        
        # 3. Oboje się poruszają (ale nie mogą iść tą samą krawędzią w przeciwnych kierunkach)
        for carol_neighbor in range(n):
            if M[u][carol_neighbor] > 0:
                for max_neighbor in range(n):
                    if M[v][max_neighbor] > 0:
                        # Sprawdź czy nie idą tą samą krawędzią w przeciwnych kierunkach
                        if not (u == max_neighbor and v == carol_neighbor):
                            new_state = (carol_neighbor, max_neighbor)
                            if new_state not in visited and shortest_path(carol_neighbor, max_neighbor) >= d:
                                visited[new_state] = True
                                parent[new_state] = current
                                queue.append(new_state)
    
    if not found:
        return None
    
    # Odtwarzanie ścieżki
    path = []
    current = end_state
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    
    return path

M = [
[0, 1, 1, 0],
[1, 0, 0, 1],
[1, 0, 0, 1],
[0, 1, 1, 0],
]
x = 0
y = 3
d = 2

#print(keep_distance(M, x, y, d))


runtests( keep_distance )
