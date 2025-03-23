from math import log10

def counting_sort(tmp, A):
    n = len(A)
    maxi = max(tmp)
    mini = min(tmp)
    count_arr = [0] * (maxi - mini + 1)

    for i in range(n):
        count_arr[tmp[i] - mini] += 1

    for i in range(1, maxi - mini + 1):
        count_arr[i] += count_arr[i - 1]
    
    result_arr = [0] * n

    for i in range(n - 1, -1, -1):
        result_arr[count_arr[tmp[i] - mini]-1] = A[i]
        count_arr[tmp[i] - mini] -= 1

    return result_arr

def key_arr(A, k): #k --> key digit
    n = len(A)
    res = [0] * n

    for i in range(n):
        key = (A[i]//10**(k))%10
        res[i] = key
    
    return res



def radix_sort(A):
    k = int(log10(max(A))) + 1

    for i in range(k):
        tmp = key_arr(A, i)
        A = counting_sort(tmp, A)

    return A



A = [53, 89, 150, 36, 633, 233]
A = radix_sort(A)
print(A)
