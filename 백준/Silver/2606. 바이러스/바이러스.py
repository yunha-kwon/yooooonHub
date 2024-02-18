comp = int(input())
link = int(input())

adjl = [[] for _ in range(comp+1)]
visited = [False] * (comp+1)
cnt = 0

def dfs(i):
    global cnt
    visited[i]= 1
    for w in adjl[i]:
        if visited[w] == 0:
            cnt += 1
            dfs(w)
    return cnt

for _ in range(link):
    c1, c2 = map(int, input().split())
    adjl[c1].append(c2)
    adjl[c2].append(c1)

print(dfs(1))