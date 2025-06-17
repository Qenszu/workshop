from zadtesty import runtests
from queue import PriorityQueue

def goodknight( G, s, t ):
  n = len(G)
  dist = [float("inf")] * n
  dist[s] = 0
  q = PriorityQueue()
  
  g = [[] for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if G[i][j] != -1:
        g[i].append((j, G[i][j]))
  G = g
  q.put((0, s, 0))

  while not q.empty():
    time, v, awake = q.get()
    print(time, v, awake)
    for u, d in G[v]:
      if awake + d > 16:
        if dist[u] > dist[v] + d + 8:
          dist[u] = dist[v] + d + 8
          q.put((dist[u], u, d))
      else:
        if dist[u] > dist[v] + d:
          dist[u] = dist[v] + d
          q.put((dist[u], u, awake + d))
      print(dist[u], u, awake, d)
        

  return dist[t]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )
