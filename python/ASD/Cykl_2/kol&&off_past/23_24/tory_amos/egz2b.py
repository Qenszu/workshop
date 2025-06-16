from egz2btesty import runtests
from queue import PriorityQueue

def tory_amos( E, A, B ):
  maxi = 0

  for v, u, time, type in E:
    maxi = max(maxi, max(u, v))

  G = [[] for _ in range(maxi+1)]
  dist = [[float("inf") for _ in range(2)] for _ in range(maxi+1)]

  for v, u, time, type in E:
    G[v].append((u, time, type))
    G[u].append((v, time, type))

  q = PriorityQueue()
  q.put((0, A))
  dist[A][0] = 0      #I track
  dist[A][1] = 0      #P track

  while not q.empty():
    time, v = q.get()
    for u, t, type in G[v]:
      flag = False
      if v == A:
        if type == 'I' and dist[u][0] > t + 5:
          dist[u][0] = t
          q.put((dist[u][0], u))
        if type == 'P' and dist[u][1] > t + 10:
          dist[u][1] = t 
          q.put((dist[u][1], u))
      if type == 'I':
        if dist[u][0] > dist[v][0] + t + 5: 
          dist[u][0] = dist[v][0] + t + 5
          flag = True
        if dist[u][0] > dist[v][1] + t + 20:
          dist[u][0] = dist[v][1] + t + 20
          flag = True
        if flag and u != B:
          q.put((dist[u][0], u))
      else:
        if dist[u][1] > dist[v][0] + t + 20:
          dist[u][1] = dist[v][0] + t + 20
          flag = True
        if dist[u][1] > dist[v][1] + t + 10:
          dist[u][1] = dist[v][1] + t + 10
          flag = True
        if flag and u != B:
          q.put((dist[u][1], u))
  
  return min(dist[B])





  # tu prosze wpisac wlasna implementacje
  return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )
E = [(0, 1, 5, 'P'), (1, 3, 1, 'I'), (3, 4, 1, 'I'),
     (2, 4, 1, 'P'), (2, 5, 1, 'I'), (0, 5, 5, 'P')]
A = 5
B = 3
#print(tory_amos(E, A, B))
