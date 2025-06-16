from egz2btesty import runtests

def magic( C ):
    n = len(C)
    f = [-1 for _ in range(n)]
    f[0] = 0

    for i in range(n):
        for j in range(1, 4):
            if C[i][j][1] != -1 and C[i][j][1] > i and f[i] != -1:
                if C[i][0] - C[i][j][0] > 10:
                    w = f[i] + 10
                else:
                    w = f[i] + C[i][0] - C[i][j][0]
                f[C[i][j][1]] = max(f[C[i][j][1]], w)
        print(f)
    return f[n-1]
    
    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = False )
C = [   [8, [ 6, 3], [ 4, 2], [7, 1]], # 0
        [22, [12, 2], [21, 3], [0,-1]], # 1
        [9, [11, 3], [ 0,-1], [7,-1]], # 2
        [15, [ 0,-1], [ 1,-1], [0,-1]] ] # 3
#magic(C)