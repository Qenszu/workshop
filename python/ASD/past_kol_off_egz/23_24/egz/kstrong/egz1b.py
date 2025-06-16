from egz1btesty import runtests


def kstrong( T, k):
    n = len(T)
    f = [[0 for _ in range(k+1)] for _ in range(n)]
    f[0][0] = max(0, T[0])
    maxi = 0

    for i in range(1, n):
        f[i][0] = max(T[i], f[i-1][0] + T[i])
        maxi = max(maxi, f[i][0])
        for j in range(1, k+1):
            if i >= j:
                f[i][j] = max(f[i-1][j-1], f[i-1][j] + T[i])
                maxi = max(maxi, f[i][j])

    return maxi


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )
