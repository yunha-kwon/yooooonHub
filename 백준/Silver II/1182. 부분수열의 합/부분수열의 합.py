N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0

for i in range(1 << N):
    subset = []
    for j in range(N):
        if i & (1 << j):
            subset.append(nums[j])

    if len(subset) > 0:
        if sum(subset) == S:
            cnt += 1

print(cnt)