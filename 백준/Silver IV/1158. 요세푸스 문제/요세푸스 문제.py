from collections import deque

N, K = map(int, input().split())

nums = deque(i for i in range(1, N+1))
result = []

while nums:
    nums.rotate(-(K-1))
    result.append(nums.popleft())

print('<', end='')
print(*result, sep=', ', end='')
print('>')
