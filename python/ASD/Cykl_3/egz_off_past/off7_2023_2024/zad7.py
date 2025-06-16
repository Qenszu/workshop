from zad7testy import runtests

def maze( L ):
    n = len(L)
    f = [[0 for _ in range(n)] for _ in range(n)]

    dirc = -1
    for j in range(n):
        dirc *= -1
        for i in range(n):
            print()
            if L[i][j] != '#':
                if dirc == 1:
                    if i + 1 < n and f[i+1][j] < f[i][j] + 1 and L[i+1][j] != '#':
                        f[i+1][j] = max(f[i][j] + 1, f[i+1][j])
                    if j + 1 < n and f[i][j+1] < f[i][j] + 1 and L[i][j+1] != '#':
                         f[i][j+1] = max(f[i][j] + 1, f[i][j+1])
                else:
                    if n-2-i >= 0 and f[n-2-i][j] < f[n-1-i][j] + 1 and L[n-2-i][j] != '#':
                        f[n-2-i][j] = max(f[n-1-i][j] + 1, f[n-2-i][j])
                    if j + 1 < n and f[n-1-i][j+1] < f[n-1-i][j] + 1 and L[n-1-i][j+1] != '#':
                         f[n-1-i][j+1] = max(f[n-1-i][j] + 1, f[n-1-i][j+1])
            for b in f:
                print(b)

    return f[n-1][n-1]            

    return 0

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( maze, all_tests = False )

L = [   "....",
        "..#.",
        "..#.",
        "...." ]
print(maze(L))