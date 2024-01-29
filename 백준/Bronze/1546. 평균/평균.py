n = int(input())
score_lst = list(map(int, input().split()))
max_num = max(score_lst)
for i in range(n):
    score_lst[i] = score_lst[i] / max_num * 100

avg = sum(score_lst) / n
print(avg)