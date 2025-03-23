def insertion_sort(A):
    for i in range(1, len(A)): 
        key = A[i]                            
        j = i - 1
        
        while j >= 0 and key < A[j]:
            A[j+1] = A[j]
            j -= 1

        A[j+1] = key

def bucket_sort(A):
    n = len(A)

    if n == 0:
        return A
    
    #creating buckets
    mini = min(A)
    maxi = max(A)
    bucket_range = (maxi - mini) / n
    buckets = [[] for _ in range(n)]

    #separating elements into buckets 
    for num in A:
        ind = int((num - mini) / bucket_range)
        if ind == n:
            ind -= 1
        
        buckets[ind].append(num)

    #sorting buckets
    sorted_A = []

    for bucket in buckets:
        insertion_sort(bucket)
        sorted_A.extend(bucket)

    return sorted_A


A = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
A = bucket_sort(A)
print("Posortowana tablica:", A)