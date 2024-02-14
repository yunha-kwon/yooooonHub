def catch_pari(x, y, dx, dy):
    global mx_val
    total = arr[y][x]
    for i in range(4):
        for j in range(1, M):
            nx = x + dx[i] * j
            ny = y + dy[i] * j

            if nx < 0 or ny < 0 or N <= nx or N <= ny: #범위 넘는 건 고려 x
                continue
            else:
                total += arr[ny][nx]

    if mx_val < total:
        mx_val = total

    return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # + 모양
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    # x 모양
    dx2 = [-1,1,-1,1]
    dy2 = [-1,1,1,-1]

    mx_val = 0
    for i in range(N):
        for j in range(N):
            catch_pari(i, j, dx, dy)
            catch_pari(i, j, dx2, dy2)

    print(f'#{tc} {mx_val}')