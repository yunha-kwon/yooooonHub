import sys
input = sys.stdin.readline

# 8방 (좌, 좌상, 상, 우상, 우, 우하, 하, 좌하) : 순서 중요!
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move = [list(map(int, input().split())) for _ in range(M)]

cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

# 1, 2, 3단계
for m in move:
    d, s = m[0] - 1, m[1] % N # 배열 범위 넘는 곳 % 연산으로 처리
    cloud_removed = [] #구름이 있다가 없어진 곳 기억해두는 용 리스트
    while cloud:
        x, y = cloud.pop()
        nx, ny = (x + dx[d] * s) % N, (y + dy[d] * s) % N
        arr[nx][ny] += 1
        cloud_removed.append((nx, ny))

# 4단계
    for x, y in cloud_removed:
        cnt = 0
        for dir in range(1, 8, 2): #대각선 방향 체크
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny]: #본인 기준 대각선에 있는 바구니에 물이 있다면
                    cnt += 1
        # 대각선 4방 탐색 후, 4방 중 물이 있는 바구니 수만큼 add
        arr[x][y] += cnt

# 5단계
    for i in range(N):
        for j in range(N):
            if (i, j) not in cloud_removed:
                if arr[i][j] >= 2:
                    cloud.append((i, j))
                    arr[i][j] -= 2

# M번 이동 후 바구니에 들어 있는 물의 양의 합 구하기
total = 0
for lst in arr:
    total += sum(lst)
    
print(total)