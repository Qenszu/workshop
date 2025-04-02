#QuickSort --> uzywa O(logn) pamieci

def partition(T, l , r):
    pivot = T[r]
    pointer = l - 1

    for i in range(l, r):
        if T[i] <= pivot:
            pointer += 1
            T[i], T[pointer] = T[pointer], T[i]
    T[r], T[pointer + 1] = T[pointer + 1], T[r]

    return pointer + 1

def quicksort(T, l , r):
    while l < r:
        pivot = partition(T, l, r)
        if pivot - l < r - pivot:
            quicksort(T, l, pivot - 1)
            l = pivot + 1
        else:
            quicksort(T, pivot + 1, r)
            r = pivot - 1

A = [2, 4, 1, 6, 3, 6, 3, 2, 9, 4, 6, 5, 3, 12, 3]
quicksort(A, 0, len(A)-1)
print(A)