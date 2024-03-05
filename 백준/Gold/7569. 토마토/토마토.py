from collections import deque

import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())

tomato = []
for _ in range(h):
    t = [list(map(int, input().split())) for _ in range(n)]
    tomato.append(t)

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dh = [0,0,0,0,1,-1]

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1: #익은 토마토라면,
                q.append([i,j,k]) #해당 인덱스를 덱에 넣어줌

while q:
    z, x, y = q.popleft()
    for dir in range(6):
        nz = z + dh[dir]
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
            if tomato[nz][nx][ny] == 0: #델타 이동한 좌표의 토마토가 익지 않았다면,
                tomato[nz][nx][ny] = tomato[z][x][y] + 1 #해당 좌표를 익은 토마토로 바꿔주고,
                q.append([nz, nx, ny]) #해당 좌표를 덱에 넣어줌

not_ripe = False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                not_ripe = True
                break

if not_ripe: #안 익은 토마토가 남아있다면
    print(-1) #-1 출력
else:
    mx = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                mx = max(tomato[i][j][k], mx)
    print(mx-1)