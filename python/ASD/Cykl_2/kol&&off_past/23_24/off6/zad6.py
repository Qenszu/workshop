from zad6testy import runtests
from queue import PriorityQueue

def jumper( G, s, w ):
    # tu prosze wpisac wlasna implementacje
    n = len(G)
    g = [[] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                g[i].append((j, G[i][j]))

    n = len(G)
    dist = [[float("inf") for _ in range(2)] for i in range(n)]
    dist[s][0] = 0
    q = PriorityQueue()
    q.put((0, s, 0))

    while not q.empty():
        d, v, jump = q.get()

        for u in range(n):
            if G[v][u] > 0:
                new_d = d + G[v][u]
                if dist[u][0] > new_d:
                    dist[u][0] = new_d
                    q.put((new_d, u, 0))
        
        if not jump:
            for u in range(n):
                for x in range(n):
                    if G[v][u] > 0 and G[u][x] > 0 and u != x:
                        new_d = d + max(G[v][u], G[u][x])
                        if dist[x][1] > new_d:
                            dist[x][1] = new_d
                            q.put((new_d, x, 1))

    return min(dist[w])

G = [[0, 1, 200, 200, 200, 200],
    [1, 0, 2, 200, 200, 200],
    [200, 2, 0, 40, 200, 200],
    [200, 200, 40, 0, 40, 200],
    [200, 200, 200, 40, 0, 117],
    [200, 200, 200, 200, 117, 0]]

#print(jumper(G, 0, 5))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )