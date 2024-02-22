def dfs(n, lst):
    if n > N: #종료조건
        if len(lst) == M: #M개짜리 수열 -> 정답
            ans.append(lst)
        return
    dfs(n+1, lst+[n])
    dfs(n+1, lst)

N, M = map(int, input().split())
ans = []
dfs(1, [])
for lst in ans:
    print(*lst)