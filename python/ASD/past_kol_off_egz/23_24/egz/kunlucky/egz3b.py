from egz3btesty import runtests


def kunlucky(T, k):
    n = len(T)
    K = [False for _ in range(n+1)]
    ind = 1

    while k <= n:
        K[k] = True
        k = k + (k % ind) + 7
        ind += 1
    
    maxi = 1
    f = [[0 for _ in range(3)] for _ in range(n)]
    if K[T[0]]:
        f[0][0] = 0    
    else:
        f[0][0] = 1
    f[0][1] = 1
    f[0][2] = 1
    
    for i in range(1, n):
        if K[T[i]]:
            f[i][0] = 0
            f[i][1] = f[i-1][0] + 1
            f[i][2] = f[i-1][1] + 1
        else:
            f[i][0] = f[i-1][0] + 1
            f[i][1] = f[i-1][1] + 1
            f[i][2] = f[i-1][2] + 1
        maxi = max(maxi, f[i][2])
    
        

    return maxi

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kunlucky, all_tests = True )


T = [11, 10, 19, 19, 17, 16, 3, 9, 6, 14, 13, 8, 2, 13, 11, 12, 5, 5, 5]
k = 3
#print(kunlucky(T, k))