n = int(input())

lst = []
for _ in range(n):
    l, h = map(int, input().split())
    lst.append([l,h])

lst.sort()

total = 0
c = 0
for a in lst:
    if a[1] > total:
        total = a[1]
        idx = c #최대 기둥 높이의 인덱스
    c += 1

#앞에서부터 최대 기둥까지
hgt = lst[0][1]

for i in range(idx):
    if hgt < lst[i+1][1]:
        total += hgt * (lst[i+1][0] - lst[i][0])
        hgt = lst[i+1][1]
    else:
        total += hgt * (lst[i+1][0] - lst[i][0])

#뒤에서부터 최대 기둥까지
hgt = lst[-1][1]

for i in range(n-1, idx, -1):
    if hgt < lst[i-1][1]:
        total += hgt * (lst[i][0] - lst[i-1][0])
        hgt = lst[i-1][1]
    else:
        total += hgt * (lst[i][0] - lst[i-1][0])

print(total)