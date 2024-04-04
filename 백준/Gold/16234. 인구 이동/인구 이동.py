import sys
input = sys.stdin.readline
from collections import deque

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    res = []
    res.append((i, j))

    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(arr[nx][ny] - arr[x][y]) <= R:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    res.append((nx, ny))

    return res

cnt = 0
while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    check = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                union = bfs(i, j)

                #print(union)
                if len(union) >= 2:
                    check = 1
                    sm = 0
                    for x, y in union:
                        sm += arr[x][y]
                    avg = sm // len(union)

                    for a, b in union:
                        arr[a][b] = avg

    if not check:
        print(cnt)
        break

    cnt += 1