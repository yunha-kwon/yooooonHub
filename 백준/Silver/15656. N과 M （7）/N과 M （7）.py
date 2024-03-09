def dfs(n):
    if n == M:
        print(*ans)
        return

    for i in range(N):
        ans.append(arr[i])
        dfs(n+1)
        ans.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []
dfs(0)
