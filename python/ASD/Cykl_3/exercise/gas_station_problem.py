"""Traktor jedzie z A do B, ma L litrow paliwa, tablica S zawiera stacje
        1. jak najmniejsza liczba tankowan
        2. paliwo na kazdej sacji ma cene za litr, dojechac jak najtaniej
        3. paliwo na kazdej sacji ma cene za litr, dojechac jak najtaniej ale zawsze tankujemy do pelna"""

#1
def sations_1(L, S):
    n = len(S)

    if n == 0:
        return 0
    if n == 1:
        return 0
    
    result = 0
    fuel = L

    for i in range(0, n-1):
        if S[i+1] - S[i] <= fuel:
            fuel -= S[i+1] - S[i]
        else:
            result += 1
            fuel = L

    return result


#2
def stations_2(L, S):
    B = len(S)
    fuel = L
    i = 0
    k = 0
    cost = 0

    while k <= B:        
        mini_cost = S[i][1]
        mini_ind = k
        k += 1
        while k < B and S[k][0] - S[i][0] <= fuel:
            if S[k][1] < mini_cost:
                mini_cost = S[k][i] 
                mini_ind = k
                break
            k += 1
        if k == B:
            mini_cost = S[i][1]
            mini_ind = k-1
        cost += S[i][1]*(S[mini_ind][0]-S[i][0])
        i = k
        k += 1
    return cost
        
#(0, 10), (5, 1), (6, 3), (8, 1)
S = [(0, 10), (5, 1), (6, 3), (8, 1)]
L = 7
print(stations_2(L, S))
