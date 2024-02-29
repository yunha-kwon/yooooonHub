P = int(input())

for _ in range(P):
    height = list(map(int, input().split()))
    stack = []
    cnt = 0

    for i in range(1, len(height)-1):
        stack.append(height[i])
        stack.sort()
        if stack[-1] > height[i+1]:
            for j in stack:
                if height[i+1] < j:
                    cnt += 1

    print(height[0], cnt)