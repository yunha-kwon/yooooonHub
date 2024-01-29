n, m = map(int, input().split())
basketNum = []
for i in range(n):
    basketNum.append(i+1)

for i in range(1, m+1):
    a, b = map(int, input().split())
    basketNum[a-1], basketNum[b-1] = basketNum[b-1], basketNum[a-1]

print(*basketNum)