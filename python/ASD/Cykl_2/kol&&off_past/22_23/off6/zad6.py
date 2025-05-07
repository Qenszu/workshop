from zad6testy import runtests

def binworker( M ):
    # tu prosze wpisac wlasna implementacje
    n = len(M)
    occupied = [-1] * n

    for i in len(n):
        flag = False
        for j in range(len(M[i])):
            if occupied[j] == -1:
                occupied[j] = M[i][j]
                flag = True
        if flag:
            pass


    return 0

M = [ [ 0, 1, 3], # 0
      [ 2, 4],    # 1
      [ 0, 2],    # 2
      [ 3, 4 ],   # 3
      [ 3, 2] ]   # 4
binworker(M)

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( binworker, all_tests = False )