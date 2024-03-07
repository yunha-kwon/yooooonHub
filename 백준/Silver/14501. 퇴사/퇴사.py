#DP로 풀기
N = int(input())

T = []
P = []
dp = [0] * (N+1)

for _ in range(N):
    Ti, Pi = map(int, input().split())
    T.append(Ti)
    P.append(Pi)

for i in range(N-1, -1, -1):
    if T[i] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[T[i] + i] + P[i])

print(dp[0])

