def sort(T):
    n = len(T)
    T = counting_sort(T, lambda x: x%n)
    T = counting_sort(T, lambda x: x//n)

    return T

def counting_sort(T, key_func):
    n = len(T)
    count = [0] * n

    for num in T:
        digit = key_func(num)
        count[digit] += 1

    for i in range(1, n):
        count[i] += count[i - 1]

    sorted_T = [0] * n
    for num in T:
        digit = key_func(num)
        count[digit] -= 1
        sorted_T[count[digit]] = num
    
    return sorted_T

T = [1, 2, 3, 4]
print(sort(T))