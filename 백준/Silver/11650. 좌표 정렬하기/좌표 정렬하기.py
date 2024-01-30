N = int(input())
lst = []

for i in range(N):
    [a, b] = map(int, input().split())
    lst.append([a, b])

lst.sort()

for i in lst:
    print(i[0], i[1])