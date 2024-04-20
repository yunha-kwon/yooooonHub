from collections import deque
da = [-1, 1, 0, 0]
db = [0, 0, -1, 1]

def move(x, y):
    q = deque()
    visited = [[0] * w for _ in range(h)]
    q.append((x, y)) # 사람의 시작 지점 q에 넣어줌
    visited[x][y] = 1 # 사람의 시작 지점 방문 표시 (1)

    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*': # 불이 있는 지점이라면
                visited[i][j] = -1 # 불이 있는 지점들 방문 표시 (-1)
                q.append((i, j)) # 불이 있는 지점들 q에 넣어줌

    while q:
        a, b = q.popleft()
        for dir in range(4):
            na = a + da[dir]
            nb = b + db[dir]
            if not (0 <= na < h and 0 <= nb < w): # 만약 영역을 벗어났다면
                if visited[a][b] > 0: # 영역을 벗어난 것이 사람이라면 (visited 배열에서의 양수)
                    return visited[a][b]

            elif 0 <= na < h and 0 <= nb < w: # 영역 안이라면
                if arr[na][nb] == '.': # 가려는 칸이 빈 공간이라면
                    if visited[a][b] > 0 and not visited[na][nb]: # 이동하려는 것이 사람(visited 배열에서의 양수)이면서, 이동하려는 칸으로 이동가능하다면,
                        visited[na][nb] = visited[a][b] + 1 # 현재 값+1을 visited 배열에 넣어준다
                        q.append((na, nb)) # 큐에 넣어줘유~

                    elif visited[a][b] < 0 and visited[na][nb] >= 0: # 이동하려는 것이 불(visited 배열에서의 음수)이면서, 이동하려는 칸으로 이동가능하다면,
                        visited[na][nb] = -1 # 이동하려는 칸을 -1(불 표시)로 바꿔준다
                        q.append((na, nb)) # 큐에 넣어줘유~

    return 'IMPOSSIBLE' # 큐가 비었는데도 탈출못했다면 임파서블이에유 ㅠ

T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    arr = []
    for _ in range(h):
        arr.append(list(map(str, input())))


    for i in range(h):
        for j in range(w):
            if arr[i][j] == '@':
                print(move(i, j))
                break