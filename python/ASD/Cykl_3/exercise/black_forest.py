def black_forest(T):
    n = len(T)
    F = [[0 for _ in range(2)] for _ in range(n+1)]

    for tree in range(1, n+1):
        F[tree][1] = F[tree-1] + T[tree-1]
        F[tree][0] = max(F[tree][0], F[tree-1][1])

    return max(F[n-1])