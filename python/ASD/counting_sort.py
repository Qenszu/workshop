def counting_sort(A):
    n = len(A)
    maxi = max(A)
    mini = min(A)
    count_arr = [0] * (maxi - mini + 1)

    for i in range(n):
        count_arr[A[i] - mini] += 1

    for i in range(1, maxi - mini + 1):
        count_arr[i] += count_arr[i - 1]
    
    result_arr = [0] * n

    for i in range(n - 1, -1, -1):
        result_arr[count_arr[A[i] - mini]-1] = A[i]
        count_arr[A[i] - mini] -= 1

    return result_arr

A = [2, 1, 4, 2, 4, 2]
A = counting_sort(A)
print(A)
    