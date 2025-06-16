from kol2testy import runtests
from queue import PriorityQueue

def warrior( G, s, t):
  n = 0
  for v, u, w in G:
    n = max(n, max(v, u))
  n += 1

  g = [[] for _ in range(n)]

  for v, u, w in G:
    g[v].append((u, w))
    g[u].append((v, w))

  dist = [[float("inf") for i in range(17)] for j in range(n)]
  for i in range(17):
    dist[s][i] = 0
  q = PriorityQueue()
  q.put((0, s, 0))

  while not q.empty():
    d, v, awake = q.get()

    for u, time in g[v]:
      if awake + time > 16:
        if dist[u][time] > dist[v][awake] + time + 8:
          dist[u][time] = dist[v][awake] + time + 8
          q.put((dist[u][time], u, time))
      else:
        if dist[u][time+awake] > dist[v][awake] + time:
          dist[u][time+awake] = dist[v][awake] + time
          q.put((dist[u][time+awake], u, time+awake))
        if dist[u][time] > dist[v][awake] + time + 8:
          dist[u][time] = dist[v][awake] + time + 8
          q.put((dist[u][time], u, time))

  for i in dist:
    print(i)

  return min(dist[t])





G = [ (1,5,10), (4,6,12), (3,2,8),
(2,4,4) , (2,0,10), (1,4,5),
(1,0,6) , (5,6,8) , (6,3,9)]
s = 0
t = 6
print(warrior(G, s, t))

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( warrior, all_tests = True )