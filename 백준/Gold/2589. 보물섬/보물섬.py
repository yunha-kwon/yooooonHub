import sys
input = sys.stdin.readline

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1
    cnt = 0

    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and arr[nx][ny] == 'L':
                visited[nx][ny] = visited[x][y] + 1
                cnt = max(visited[nx][ny], cnt)
                q.append([nx, ny])

    return cnt-1

N, M = map(int, input().split()) #세로, 가로
arr = [list(input().strip()) for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result)