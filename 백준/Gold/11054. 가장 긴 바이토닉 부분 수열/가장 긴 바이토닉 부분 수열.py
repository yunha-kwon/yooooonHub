n = int(input())
arr = list(map(int, input().split()))
r_arr = arr[::-1]

dp = [1] * n
r_dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

        if r_arr[i] > r_arr[j]:
            r_dp[i] = max(r_dp[i], r_dp[j]+1)

r_dp = r_dp[::-1]

res = []
for i in range(n):
    res.append(r_dp[i] + dp[i] - 1)

print(max(res))