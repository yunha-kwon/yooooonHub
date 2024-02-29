def cnt_mx():
    row_cnt = col_cnt = 1
    row_max = col_max = 0

    for i in range(N):
        for j in range(N-1):
            if arr[i][j] == arr[i][j+1]:
                row_cnt += 1
            else:
                row_cnt = 1
            row_max = max(row_cnt, row_max)
        row_cnt = 1

    for j in range(N):
        for i in range(N-1):
            if arr[i][j] == arr[i+1][j]:
                col_cnt += 1
            else:
                col_cnt = 1
            col_max = max(col_cnt, col_max)
        col_cnt = 1

    ans = max(row_max, col_max)
    return ans

N = int(input())
arr = [list(input()) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = 0
for i in range(N):
    for j in range(N):
        for dir in range(4):
            nx = i + dx[dir]
            ny = j + dy[dir]
            if not (0 <= nx < N and 0 <= ny < N):
                break
            if arr[i][j] != arr[nx][ny]:
                arr[i][j], arr[nx][ny] = arr[nx][ny], arr[i][j]
                result = max(result, cnt_mx())
                arr[i][j], arr[nx][ny] = arr[nx][ny], arr[i][j]

print(result)