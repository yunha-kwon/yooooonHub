N, M = map(int, input().split())
arr = [[] for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input()))

ans = []
if N >= M:
    tmp = M
else:
    tmp = N

i = 0
j = 0

while tmp > 0:
    if arr[i][j] == arr[i+tmp-1][j] == arr[i][j+tmp-1] == arr[i+tmp-1][j+tmp-1]:
        ans.append(tmp**2)
    j += 1

    if j+tmp-1 >= M:
        j = 0
        i += 1

    if i+tmp-1 >= N:
        tmp -= 1
        i = 0
        j = 0

print(max(ans))