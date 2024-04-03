# 로봇 청소기
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
cnt = 0 #로봇 청소기가 청소한 칸 수

# 북 동 남 서 (순서 중요)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

q = deque()
q.append((r, c)) #큐에 시작 지점 넣어주기
visited[r][c] = 1 #시작 지점 방문 표시
cnt += 1

def bfs(d):
    global cnt
    while q:
        x, y = q.popleft()
        changed_dir = 0

        for _ in range(4):
            d = (d + 3) % 4
            # 북쪽 0 -> 서쪽 3
            # 동쪽 1 -> 북쪽 0
            # 서쪽 3 -> 남쪽 2
            # 남쪽 2 -> 동쪽 1
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0 and visited[nx][ny] != 1:
                visited[nx][ny] = 1 #방문 표시
                cnt += 1
                q.append((nx, ny)) #그 다음 지점 큐에 넣어주기
                changed_dir = 1 #반시계 방향 전환 다 해봤음 표시
                break

        # 4방향 다 탐색 해도 청소 가능한 곳이 없는 경우
        if changed_dir == 0:
            if arr[x - dx[d]][y - dy[d]] == 0: #현재 방향 그대로 후진이 가능하다면,
                q.append((x - dx[d], y - dy[d])) #후진한다!
            else: #현재 방향 그대로 후진이 불가능하다면,
                return cnt #정답 반환

bfs(d)
print(cnt)