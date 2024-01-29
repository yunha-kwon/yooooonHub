n, m = map(int, input().split())
basketNum = [0] * n
for i in range(n):
    basketNum[i] = i+1

for i in range(m):
    r1, r2 = map(int, input().split())
    range_swap = basketNum[r1-1:r2]
    range_swap.reverse()
    basketNum[r1-1:r2] = range_swap

print(*basketNum)