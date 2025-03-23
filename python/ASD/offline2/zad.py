def func(arr):
    cnt = 0
    def merge_sort(arr):
        nonlocal cnt
        size = len(arr)
        if size > 1:
            left_arr = arr[:size//2]
            right_arr = arr[size//2:]

            merge_sort(left_arr)
            merge_sort(right_arr)

            i = 0 
            j = 0
            k = 0
            tmp = 0
            multi = 0
            flag = False
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    cnt += len(left_arr) - i
                    arr[k] = right_arr[j]
                    j += 1
                k += 1

            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1                                                        
                k += 1                                                           

            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1

    merge_sort(arr)
    return cnt


arr_test = [1,20,6,4,5]
cnt = 0
print(func(arr_test))