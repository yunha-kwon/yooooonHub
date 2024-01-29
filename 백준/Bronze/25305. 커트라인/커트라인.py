N, k = map(int, input().split())
scores = map(int, input().split())

score_lst = []

for i in scores:
    score_lst.append(i)

score_lst.sort(reverse=True) 
print(score_lst[k-1])