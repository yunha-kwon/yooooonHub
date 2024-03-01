import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque(enumerate(map(int, input().split())))
result = []

while q:
    idx, num = q.popleft()
    result.append(idx+1)

    if num > 0:
        q.rotate(-(num-1))
    else:
        q.rotate(-num)

print(*result)