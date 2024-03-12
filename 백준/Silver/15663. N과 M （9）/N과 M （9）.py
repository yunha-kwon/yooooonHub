def dfs():
    if len(ans) == M:
        print(*ans)
        return

    tmp = 0
    for i in range(N):
        if not visited[i] and tmp != arr[i]:
            visited[i] = True
            ans.append(arr[i])
            tmp = arr[i]
            dfs()
            visited[i] = False
            ans.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []
visited = [False] * N
dfs()
