arr = []
for i in range(9):
    arr.append(int(input()))

arr.sort() #정렬
sum = sum(arr)

ans_lst = []
a = False
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if sum - arr[i] - arr[j] == 100:
            a = True
            for k in range(len(arr)):
                if k == i or k == j:
                    continue
                else:
                    print(arr[k])

            break
    if a: break