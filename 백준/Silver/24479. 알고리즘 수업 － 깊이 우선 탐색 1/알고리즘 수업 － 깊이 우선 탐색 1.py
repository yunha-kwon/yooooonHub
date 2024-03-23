def dfs(start):
    global cnt
    visited[start] = cnt
    for w in graph[start]:
        if not visited[w]:
            cnt += 1
            dfs(w)


import sys
input = sys.stdin.readline
sys.setrecursionlimit(150000)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
cnt = 1
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for lst in graph:
    lst.sort()

dfs(R)
for i in range(1, N + 1):
    print(visited[i])
