N, M = map(int, input().split())
board = []
lst = []

for _ in range(N):
    board.append(input())

for i in range(N-7):
    for j in range(M-7):
        black = 0
        white = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x + y) % 2 == 0:
                    if board[x][y] != 'B':
                        black += 1
                    if board[x][y] != 'W':
                        white += 1

                else:
                    if board[x][y] != 'W':
                        black += 1
                    if board[x][y] != 'B':
                        white += 1

        lst.append(black)
        lst.append(white)

print(min(lst))