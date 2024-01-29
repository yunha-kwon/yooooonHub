import sys
input = sys.stdin.readline

N = int(input().rstrip())
dominos = [list(map(int, input().rstrip().split())) for _ in range(N)]
cnt = 1

dominos.sort(key=lambda x: x[0])

x_max = dominos[0][0] + dominos[0][1]

for i in range(1, N):
    current_x, current_length = dominos[i]

    if current_x > x_max:
        cnt += 1
      
   
    x_max = current_x + current_length

print(cnt)