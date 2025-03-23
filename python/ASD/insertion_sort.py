def insertion_sort(A):
    for i in range(1, len(A)): 
        key = A[i]                            
        j = i - 1
        
        while j >= 0 and key < A[j]:
            A[j+1] = A[j]
            j -= 1

        A[j+1] = key


A = [5, 3, 8, 6, 2]
insertion_sort(A)
print("Posortowana tablica:", A)