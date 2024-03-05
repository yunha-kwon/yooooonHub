import sys
input = sys.stdin.readline

N = int(input())
tar1, tar2 = map(int, input().split())
M = int(input())

chonsu = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
result = []

for i in range(M):
    x, y = map(int, input().split())
    chonsu[x].append(y)
    chonsu[y].append(x)

flag = False
def dfs(x, cnt):
    global flag
    visited[x] = 1
    if x == tar2:
        flag = True
        print(cnt)
    for i in chonsu[x]:
        if visited[i] == 0:
            dfs(i, cnt+1)


dfs(tar1, 0)

if not flag:
    print(-1)