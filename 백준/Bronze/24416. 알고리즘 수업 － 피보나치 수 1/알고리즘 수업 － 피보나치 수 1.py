def fibo_recur(n):
    global cnt1
    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    else:
        return (fibo_recur(n - 1) + fibo_recur(n - 2))

def fibo_dp(n):
    global cnt2
    dp = [0] * (n + 1)
    dp[1] = dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        cnt2 += 1
    return dp[n]

n = int(input())

cnt1 = cnt2 = 0
fibo_recur(n)
print(cnt1)
fibo_dp(n)
print(cnt2)