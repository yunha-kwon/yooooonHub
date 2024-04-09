# 미세먼지 안녕!
from pprint import pprint
import copy
import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

#room2 = copy.deepcopy(room)

# 1. 미세먼지의 확산... (이건 할만 해!)
def diffusion(room):
    room2 = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if room[i][j] != 0 and room[i][j] != -1:
                cnt = 0
                for dir in range(4):
                    ni = i + dx[dir]
                    nj = j + dy[dir]
                    if 0 <= ni < R and 0 <= nj < C and room[ni][nj] != -1:
                        room2[ni][nj] += room[i][j] // 5
                        cnt += 1
                room2[i][j] += room[i][j]
                room2[i][j] -= (room[i][j] // 5) * cnt

            if room[i][j] == -1:
                room2[i][j] = -1

    return room2

purifier = [] # 공기청정기 인덱스 저장
for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            purifier.append((i, j))

# 2. 공기청정기의 작동... (이게 너무 헷갈려!)
def rotate(room2):
    up_x, up_y = purifier[0]
    down_x, down_y = purifier[1]
    room3 = [[0] * C for _ in range(R)]
    # 위
    for j in range(2, C):
        room3[up_x][j] = room2[up_x][j-1]
    room3[up_x][1] = 0
    for i in range(0, up_x):
        room3[i][-1] = room2[i+1][-1]
        if i != 0:
            for j in range(1, C-1):
                room3[i][j] = room2[i][j]
    for j in range(0, C-1):
        room3[0][j] = room2[0][j+1]
    for i in range(1, up_x):
        room3[i][0] = room2[i-1][0]
    
    # 아래
    for j in range(2, C):
        room3[down_x][j] = room2[down_x][j-1]
    room3[down_x][1] = 0
    for i in range(down_x+1, R):
        room3[i][-1] = room2[i-1][-1]
    for j in range(C-1):
        room3[-1][j] = room2[-1][j+1]
    for i in range(down_x+1, R-1):
        room3[i][0] = room2[i+1][0]
        for j in range(1, C-1):
            room3[i][j] = room2[i][j]

    return room3

for _ in range(T):
    tmp = diffusion(room)
    room = rotate(tmp)

total = 0
for lst in room:
    total += sum(lst)
print(total)
