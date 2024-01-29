arr = []
for i in range(9):
    arr.append(list(map(int, input().split())))

max_lst = []
max_index = []
for row in arr:
    max_lst.append(max(row))

max_num = max(max_lst)
print(max_num)


for row in arr:
    if max_num in row:
        print(arr.index(row) + 1, row.index(max_num) + 1)