def dfs(n):
    if len(ans) == M:
        print(*ans)
        return

    for i in range(n, N):
        if arr[i] not in ans:
            ans.append(arr[i])
            dfs(i+1)
            ans.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []
dfs(0)
