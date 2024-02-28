hor, ver = map(int, input().split())
hor = [0, hor] #[0, 10]
ver = [0, ver] #[0, 8]

cut = int(input())
for _ in range(cut):
    dir, num = map(int, input().split())

    if dir == 0: #가로로 자르기
        ver.append(num)
    elif dir == 1: #세로로 자르기
        hor.append(num)

hor.sort()
ver.sort()

ans = 0

for i in range(len(hor)-1):
    for j in range(len(ver)-1):
        ans = max(ans, (ver[j+1] - ver[j]) * (hor[i+1] - hor[i]))

print(ans)