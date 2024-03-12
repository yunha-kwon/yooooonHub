def dfs(n):
    if len(ans) == M:
        print(*ans)
        return

    for i in range(n, N):
        ans.append(arr[i])
        dfs(i)
        ans.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []
dfs(0)
