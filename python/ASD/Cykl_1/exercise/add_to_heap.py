def heapify(A, n, i):
    maxi = i
    left = 2 * i + 1
    right = 2 * i + 2


    if left < n and A[left] > A[maxi]:
        maxi = left
    if right < n and A[right] > A[maxi]:
        maxi = right

    if maxi != i:
        A[i], A[maxi] = A[maxi], A[i]
        heapify(A, n, maxi)

def add_to_heap(A, val):
    A.append(val)
    n = len(A)

    A[0], A[n-1] = A[n-1], A[0]

    #print(A)
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)
    return A

A = [95, 84, 72, 63, 58, 41, 65, 22, 47]
A = add_to_heap(A, 76)
#print(A)



    