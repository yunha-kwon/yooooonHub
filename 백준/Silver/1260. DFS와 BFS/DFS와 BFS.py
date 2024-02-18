from collections import deque

V, E, i = map(int, input().split())
adjl = [[] for _ in range(V+1)]
visited_dfs = [0] * (V+1)
visited_bfs = [0] * (V+1)
for _ in range(E):
    v1, v2 = map(int, input().split())
    adjl[v1].append(v2)
    adjl[v2].append(v1)

for a in adjl:
    a.sort()

def dfs(i):
    visited_dfs[i] = 1
    print(i,end=' ')
    for u in adjl[i]:
        if visited_dfs[u] == 0:
            dfs(u)

def bfs(i):
    q = deque([i])
    visited_bfs[i] = 1
    while q:
        i = q.popleft()
        print(i,end=' ')
        for w in adjl[i]:
            if visited_bfs[w] == 0:
                q.append(w)
                visited_bfs[w] = 1

dfs(i)
print()
bfs(i)