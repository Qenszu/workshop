from egz1btesty import runtests

def planets( D, C, T, E ):
    n = len(D)
    f = [[float("inf") for _ in range(E+1)] for _ in range(n)]
    
    for i in range(E+1):
        f[0][i] = i * C[0]
    if T[0][0] != 0:
        f[T[0][0]][0] = T[0][1]

    for i in range(1, n):
        for b in range(E+1):
            if T[i][0] != i:
                f[T[i][0]][0] = min(T[i][1] + f[i][0], f[T[i][0]][0])
            if D[i]-D[i-1]+b < E+1:
                f[i][b] = min(f[i][b], min(f[i-1][D[i]-D[i-1]+b], f[i][max(0, b-1)] + C[i]))
            else:
                f[i][b] = min(f[i][b], f[i][max(0, b-1)] + C[i])

    return f[n-1][0]


    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
