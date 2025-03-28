from zad1testy import runtests

def partition(A, p, r):
    if p < r:
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        
        A[i+1], A[r] = A[r], A[i+1]
        return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

def make_1D_arry(A):
    n = len(A)
    result = [0 for _ in range(n*n)]

    for i in range(n):
        for j in range(n):
            result[n*i + j] = A[i][j]

    return result

def sume_func(n):
    result = 0

    for i in range(n):
        result += i

    return result
    
def median(A):
    T = make_1D_arry(A)
    quicksort(T, 0, len(T)-1)
    n = len(A)
    start_half =  sume_func(n)
    start_ind = 0
    tail_ind = n * n - 1

    for i in range(n):
        for j in range(n):
            if i == j:
                A[i][j] = T[start_half]
                start_half += 1
            elif i < j:
                A[i][j] = T[tail_ind]
                tail_ind -= 1
            else:
                A[i][j] = T[start_ind]
                start_ind += 1


runtests(median)
