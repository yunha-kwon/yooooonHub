import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
sorted_lst = sorted(set(lst))

dic = {sorted_lst[i]:i for i in range(len(sorted_lst))}

for i in lst:
    print(dic[i], end=' ')