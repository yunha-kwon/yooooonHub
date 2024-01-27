def merge_and_sort_arrays(arr_a, arr_b):
    result = []
    i, j = 0, 0

    while i < len(arr_a) and j < len(arr_b):
        if arr_a[i] < arr_b[j]:
            result += [arr_a[i]]
            i += 1
        else:
            result += [arr_b[j]]
            j += 1

    while i < len(arr_a):
        result += [arr_a[i]]
        i += 1

    while j < len(arr_b):
        result += [arr_b[j]]
        j += 1

    return result

n, m = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

result_array = merge_and_sort_arrays(arr_a, arr_b)

for num in result_array:
    print(num, end=' ')
