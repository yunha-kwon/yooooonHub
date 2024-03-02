n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

mn = n * m

cnt = 0
for w in range(0, n-2): #white
    for i in range(0, m):
        if arr[w][i] != 'W':
            cnt += 1

    cnt2 = 0
    for b in range(w+1, n-1): #blue
        for i in range(0, m):
            if arr[b][i] != 'B':
                cnt2 += 1

        cnt3 = 0
        for r in range(b+1, n): #red
            for i in range(0, m):
                if arr[r][i] != 'R':
                    cnt3 += 1

        total = cnt + cnt2 + cnt3

        if mn > total:
            mn = total

print(mn)
