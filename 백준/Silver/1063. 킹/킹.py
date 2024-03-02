king, stone, move_num = input().split()

move = {'R':(0,1), 'L':(0,-1), 'B':(1,0), 'T':(-1,0), 'RT':(-1,1), 'LT':(-1,-1), 'RB':(1,1), 'LB':(1,-1)}
chess = ['A','B','C','D','E','F','G','H'] #가로 위치값
kx, ky = (8-int(king[1])), chess.index(king[0])
sx, sy = (8-int(stone[1])), chess.index(stone[0])

for _ in range(int(move_num)):
    command = input()
    x, y = move[command]
    if 0 <= kx + x < 8 and 0 <= ky + y < 8:
        kx, ky = kx + x, ky + y
        if kx == sx and ky == sy:
            sx, sy = sx + x, sy + y

    if not (0 <= sx < 8 and 0 <= sy < 8):
        kx, ky = kx - x, ky - y
        sx, sy = sx - x, sy - y

print(chess[ky], 8-kx, sep='')
print(chess[sy], 8-sx, sep='')