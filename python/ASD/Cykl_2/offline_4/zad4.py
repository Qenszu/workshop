from zad4testy import runtests
from queue import PriorityQueue


def dijkstra(G, start, end):
    #relaxation
    def relaxation(v,u,weight):
        if(dist[u]>dist[v]+weight):
            dist[u]=dist[v]+weight
            return True
        return False

    n = len(G)
    dist = [float('inf') for _ in range(n)]

    q = PriorityQueue()
    q.put((0,start))
    dist[start]=0
    
    while not q.empty():
        cost, v = q.get()
        for u,weight in G[v]:
            if(relaxation(v,u,weight)):
                q.put((dist[u],u))
    print(dist)
    return dist[end]


def spacetravel( n, E, S, a, b ):

    G = [[] for _ in range(n+1)]
    for v, u, cost in E:
        G[v].append((u, cost))
        G[u].append((v, cost))

    for v in S:
        G[v].append((n, 0))
        G[n].append((v, 0))

    result = dijkstra(G, a, b)
    if result == float("inf"):
        return None
    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
