dp = [1] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, 101):
    dp[i] = dp[i-3] + dp[i-2]

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N])