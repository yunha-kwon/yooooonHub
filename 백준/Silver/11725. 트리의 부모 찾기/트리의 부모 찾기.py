import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
adjl = [[] for _ in range(N+1)]

for _ in range(N-1):
    v1, v2 = map(int, input().split())
    adjl[v1].append(v2)
    adjl[v2].append(v1)

visited = [0]*(N+1)

def dfs(v):
    for i in adjl[v]:
        if not visited[i]:
            visited[i] = v
            dfs(i)

dfs(1)

for i in range(2, N+1):
    print(visited[i])