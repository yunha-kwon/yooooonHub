import sys
input = sys.stdin.readline

n = int(input())
edges = [list(map(int, input().split())) for _ in range(n)]
edges = sorted(edges, key=lambda x: x[0]) #첫번째 정점을 기준으로 오름차순 정렬

#print(edges)
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if edges[j][1] < edges[i][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))