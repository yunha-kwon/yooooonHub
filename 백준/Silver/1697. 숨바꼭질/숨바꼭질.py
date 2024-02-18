#숨바꼭질
from collections import deque

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(pos[x])
            break
        for next_x in (x-1, x+1, 2*x):
            if 0 <= next_x <= 10 ** 5 and not pos[next_x]:
                pos[next_x] = pos[x] + 1
                q.append(next_x)

N, K = map(int, input().split())
pos = [0] * (10 ** 5 + 1)
bfs()