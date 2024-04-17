import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

sm_lst = [0]
cnt = 0

for i in range(N):
    cnt += nums[i]
    sm_lst.append(cnt)

for _ in range(M):
    i, j = map(int, input().split())
    print(sm_lst[j]-sm_lst[i-1])