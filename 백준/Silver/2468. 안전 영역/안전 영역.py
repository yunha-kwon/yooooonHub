import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y, w):
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] > w:
            visited[nx][ny] = True
            dfs(nx, ny, w)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

ans = 1
for w in range(max(map(max, board))):
    visited = [[False] * n for _ in range(n)]
    safe = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > w and not visited[i][j]:
                safe += 1
                visited[i][j] = True
                dfs(i, j, w)
    ans = max(ans, safe)

print(ans)