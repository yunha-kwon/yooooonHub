lst_x = []
lst_y = []

for i in range(3):
    x, y = map(int, input().split())
    lst_x.append(x)
    lst_y.append(y)

ans_lst = []

for i in lst_x:
    if lst_x.count(i) == 1:
        ans_lst.append(i)

for i in lst_y:
    if lst_y.count(i) == 1:
        ans_lst.append(i)

print(*ans_lst)