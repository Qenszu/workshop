from kol2btesty import runtests


def min_cost( O, C, T, L ):
    # tu prosze wpisac wlasna implementacje

    n = len(O)

    for i in range(n):
        O[i] = (O[i], C[i])
    
    O.append((L, 0))
    n += 1
    O.sort(key=lambda x: x[0])

    Z = [float("inf")] * n                  #Z 2 zasada
    Z[0] = 0
    B = [0] * n                             #BEZ 2 zasady  
    crr_distance_B = T - O[0][0]            #dostepne kilometry bez postoju    


    for i in range(1, n):
        if crr_distance_B + O[i-1][0] < O[i][0]:
            B[i] = B[i-1] + O[i-1][1]
            crr_distance_B = T - (O[i][0] - O[i-1][0])
        else:
            B[i] = B[i-1]
            crr_distance_B -= O[i][0] - O[i-1][0]
        if O[i][0] <= 2 * T:
            Z[i] = 0
        else:
            ind = i - 1
            while O[i][0] - O[ind][0] <= T and ind > -1:
                Z[i] = min(Z[i], Z[ind] + O[ind][1])
                ind -= 1
            ind = i - 1
            while O[i][0] - O[ind][0] <= 2 * T and ind > -1:
                Z[i] = min(Z[i], O[ind][1] + B[ind])
                ind -= 1

    #print(B, Z)

    return Z[n-1]


O = [17, 20, 11,  5, 12] 
C = [9, 7, 7, 7,  3] 
T  =  7 
L =  25
#print(min_cost(O, C, T, L))

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( min_cost, all_tests = True )