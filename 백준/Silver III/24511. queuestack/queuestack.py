import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

q = deque([])

for i in range(N):
    if A[i] == 0:
        q.appendleft(B[i])

if q == []:
    print(*C)

for i in range(M):
    q.append(C[i])
    print(q.popleft(), end=' ')



