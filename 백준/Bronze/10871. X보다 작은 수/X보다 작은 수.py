n, x = map(int, input().split())
a_lst = list(map(int, input().split()))

for i in a_lst:
    if i < x:
        print(i, end=' ')