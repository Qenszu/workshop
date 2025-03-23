def heapify_rek(arr, size, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < size and arr[left] > arr[largest]:
        largest = left

    if right < size and arr[right] > arr[largest]:
        largest = right 

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_rek(arr, size, largest)

def heapify_ite(arr, size, i):
    while True:
        largest = i  
        left = 2 * i + 1  
        right = 2 * i + 2  

        if left < size and arr[left] > arr[largest]:
            largest = left

        if right < size and arr[right] > arr[largest]:
            largest = right

    
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest  
        else:
            break  

def heapsort(arr):
    size = len(arr)


    for i in range(size // 2 - 1, -1, -1):
        heapify_rek(arr, size, i)

    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify_rek(arr, i, 0)

arr = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]
heapsort(arr)
print("Posortowana tablica:", arr)