C, R = map(int, input().split()) #공연장의 격자 크기
K = int(input()) #대기번호

hall = [[0] * C for _ in range(R)]

#위-오른쪽-아래-왼쪽
dx = [-1,0,1,0]
dy = [0,1,0,-1]

cnt = 1
k = 0

sx = R-1
sy = 0
hall[sx][sy] = 1

while True:
    if cnt == C * R:
        break

    nx = sx + dx[k]
    ny = sy + dy[k]

    if 0 <= nx < R and 0 <= ny < C and hall[nx][ny] == 0:
        cnt += 1
        hall[nx][ny] = cnt
        sx = nx
        sy = ny

    else:
        k += 1
        if k >= 4:
            k = k % 4

for i in range(R):
    for j in range(C):
        if hall[i][j] == K:
            print(j+1, R-i)

if K > C * R:
    print(0)