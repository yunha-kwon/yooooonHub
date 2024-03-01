bingo = [list(map(int, input().split())) for _ in range(5)]
nums = [list(map(int, input().split())) for _ in range(5)]
cnt = 0

dx = [0,1,1,1]
dy = [1,0,-1,1]

def check_bingo(bingo):
    result = 0
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == 0:
                for dir in range(4):
                    ni = i
                    nj = j
                    cnt = 0

                    while 0 <= ni < 5 and 0 <= nj < 5 and bingo[ni][nj] == 0:
                        cnt += 1
                        ni += dx[dir]
                        nj += dy[dir]

                    if cnt == 5:
                        result += 1

    if result >= 3:
        return True
    else:
        return False


for i in range(5):
    for j in range(5):
        num = nums[i][j]
        for x in range(5):
            for y in range(5):
                if num == bingo[x][y]:
                    bingo[x][y] = 0
                    cnt += 1
                    if check_bingo(bingo):
                        print(cnt)
                        exit()
                        


