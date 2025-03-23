def quickselect(A, p, r, k):
    if p == r:
        return A[p]
    
    q = partition(A, p, r)
    
    if k  == q:
        return A[q]
    elif k  < q:
        return quickselect(A, p, q - 1, k)
    else:
        return quickselect(A, q + 1, r, k)
        
        

def partition(A, p, r):
    pivot = A[r]
    i = p - 1
    
    for j in range(p, r):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
        
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

A = [1, 3, 4, 2]
k = 3
n = len(A)
print(k, "-ty elemento to: ", quickselect(A, 0, n - 1, n-k))