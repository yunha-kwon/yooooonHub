def dfs(n):
    if len(ans) == M:
        print(*ans)
        return

    tmp = 0
    for i in range(n, N):
        if not visited[i] and tmp != arr[i]:
            visited[i] = True
            ans.append(arr[i])
            tmp = arr[i]
            dfs(i+1)
            visited[i] = False
            ans.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []
visited = [False] * N
dfs(0)
