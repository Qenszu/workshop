from zad7testy import runtests


def orchard(T, m):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    f = [[float('inf') for _ in range(m)] for _ in range(n)]
    f[0][0] = 1
    f[0][T[0]%m] = 0
    for i in range(1,n):
        for j in range(m):
            f[i][j] = min(f[i-1][(j-T[i]+m)%m], f[i-1][j] + 1)
    minimum = f[n-1][0]
    return minimum


# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests(orchard, all_tests=False)
T = [2, 2, 7, 5, 1, 14, 7]
m = 7

print(orchard(T, m))