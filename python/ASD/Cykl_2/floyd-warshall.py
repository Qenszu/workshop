def floyd_warshall(G):
    n = len(G)
    dist = [[float("inf")] * n for _ in range(n)]
    next_node = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j: 
                dist[i][j] = 0
            elif G[i][j] is not None:
                dist[i][j] = G[i][j]
                next_node[i][j] = j

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    min_c = float("inf")
    ind = -1
    for i in range(n):
        if dist[i][i] < min_c:
            min_c = dist[i][i]
            ind = i
        
    if ind == -1:
        return None
    
    cycle = []
    current = ind
    while True:
        cycle.append(current)
        current = next_node[current][ind]
        if current == ind and len(cycle) > 1:
            return cycle
        if len(cycle) > n:
            return None