N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

result = []

def dfs(n):
    if n == M:
        print(*result)
        return

    tmp = 0
    for i in range(N):
        if tmp != nums[i]:
            result.append(nums[i])
            tmp = nums[i]
            dfs(n+1)
            result.pop()

dfs(0)