from egz3atesty import runtests
from queue import PriorityQueue

def mykoryza( G,T,d ):
    n = len(G)
    occ = [-1 for _ in range(n)]
    q = PriorityQueue()
    cnt = 1
    i = 0
    for m in T:
        occ[m] = m
        q.put((0, i, m))
        i += 1

    while not q.empty():
        time, m, tree = q.get()

        for u in G[tree]:
            if occ[u] == -1:
                occ[u] = m
                q.put((time+1, m, u))
                if m == d:
                    cnt += 1

    return cnt

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza, all_tests = True )
G = [[1,3],[0,2,4],[1,5],
 [0,4,6],[1,3,5,7],[2,4,8],
 [3,7],[4,6,8],[7,5]]
T = [8,2,6]
d = 1
#print(mykoryza(G, T, d))