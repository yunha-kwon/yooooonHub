import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temp_lst = list(map(int, input().split()))

sum_lst = []
sum_lst.append(sum(temp_lst[:K]))

for i in range(N-K):
    sum_lst.append(sum_lst[i] - temp_lst[i] + temp_lst[K+i])

print(max(sum_lst))