L = int(input()) #롤케이크 길이
N = int(input()) #방청객 수

rollcake = [0] * (L+1)
lst = []
for i in range(1, N+1):
    p, k = map(int, input().split())
    lst.append(k+1-p)
    for j in range(p, k+1):
        if rollcake[j] == 0:
            rollcake[j] = i

lst2 = []
for i in range(1, N+1):
    c = rollcake.count(i)
    lst2.append(c)

print(lst.index(max(lst)) + 1) #가장 많은 조각을 받을 것으로 기대하고 있던 방청객 번호
print(lst2.index(max(lst2)) + 1) #실제로 가장 많은 조각을 받은 방청객 번호
