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
    dist[s][0] = dist[s][1] = 0
    q = PriorityQueue()
    q.put((0, s, 0))

    while not q.empty():
        d, v, jump = q.get()

        if jump:
            for u, weight in g[v]:
                if dist[u][jump] > dist[v][jump] + weight:
                    dist[u][jump] = dist[v][jump] + weight
                    q.put((dist[u][jump], u, 0))
        else:
            for u, weight in g[v]:
                if dist[u][jump] > dist[v][jump] + weight:
                    dist[u][jump] = dist[v][jump] + weight
                    q.put((dist[u][jump], u, 0))
                for x, weight_2 in g[u]:
                    if dist[x][1] > dist[v][jump] + max(weight, weight_2):
                        dist[x][1] = dist[v][jump] + max(weight, weight_2)
                        q.put((dist[x][1], x, 1))
    
    return min(dist[w])

    return None


G = [   [0, 1, 200, 200, 200, 200],
        [1, 0, 2, 200, 200, 200],
        [200, 2, 0, 40, 200, 200],
        [200, 200, 40, 0, 40, 200],
        [200, 200, 200, 40, 0, 117],
        [200, 200, 200, 200, 117, 0]]

#print(jumper(G, 0, 5))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )