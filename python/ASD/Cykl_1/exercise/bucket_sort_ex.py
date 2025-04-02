""""Najwieksza roznica
    A - tablica n - elementowa, prarami rozne
    Znalezc takie x,y ze nie istenieje z: x < z < y oraz
    roznica x i y jest najwieksza"""

def max_diff(T):
    n = len(T)
    if n < 2:
        return 0
    
    high = max(T)
    low = min(T)
    run = high - low
    bucket = [[] for _ in range(n)]
    ind = 0

    for num in T:
        if num == high:
            ind = n-1
        else:
            ind = (num - low) * (n-1) // run
        bucket[ind].append(num)
    res_bucket = []
    for i in range(n):
        if bucket[i]:
            res_bucket.append((min(bucket[i]), max(bucket[i])))
    
    maxi = 0
    result = ()
    for i in range(i, len(res_bucket)):
        tmp = maxi
        maxi = max(maxi, len(res_bucket[i-1][1]-res_bucket[i][0]))
        if tmp != maxi:
            result = (res_bucket[i-1][1], res_bucket[i][0])
    return result

T = [1, 2, 3, 5]
print(max_diff(T))