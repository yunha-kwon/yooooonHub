from collections import deque
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

def bfs(arr, i, j):
    #상하좌우 델타탐색
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    q = deque()
    q.append((i, j))
    arr[i][j] = 0 #방문한 곳은 0으로 바꿔서 다시 방문하지 못하도록 함
    cnt = 1

    while q:
        i, j = q.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if arr[nx][ny] == 1: #다음 탐색 지점이 1(집이 있는 곳)이라면,
                arr[nx][ny] = 0 #방문한 곳은 0으로 바꿔서 다시 방문하지 못하도록 함
                q.append((nx, ny))
                cnt += 1

    return cnt

result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            result.append(bfs(arr, i, j))

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])