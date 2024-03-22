# 정수 삼각형
n = int(input())
dp = []

for i in range(n):
    dp.append(list(map(int,input().split())))

#print(dp)

for i in range(1, n): #i: 1/2/3/4
    for j in range(i+1): #j: 0~1/0~2/0~3/0~4
        if j == 0 : #제일 왼쪽 열
            dp[i][0] += dp[i-1][0]
        elif j == i: #빗변 열
            dp[i][j] += dp[i-1][j-1]
        else: #그 사이 어딘가
            dp[i][j] += max(dp[i-1][j-1],dp[i-1][j])

#print(dp)
print(max(dp[n-1]))