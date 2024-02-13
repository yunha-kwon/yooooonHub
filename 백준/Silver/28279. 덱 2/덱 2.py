import sys
from collections import deque
n = int(input())

q = deque()
for i in range(n):
    command = list(map(int, sys.stdin.readline().strip().split()))
    l = len(q)
    if command[0] == 1:
        q.appendleft(command[1])
    elif command[0] == 2:
        q.append(command[1])
    elif command[0] == 3:
        print(q.popleft() if l else -1)
    elif command[0] == 4:
        print(q.pop() if l else -1)
    elif command[0] == 5:
        print(len(q))
    elif command[0] == 6:
        print(0 if l else 1)
    elif command[0] == 7:
        print(q[0] if l else -1)
    elif command[0] == 8:
        print(q[-1] if l else -1)