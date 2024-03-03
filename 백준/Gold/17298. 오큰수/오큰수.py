n = int(input())

lst = list(map(int, input().split()))

result = [-1] * n
stack = [0]

for i in range(1, n):
    while stack:
        if lst[stack[-1]] < lst[i]:
            idx = stack.pop()
            result[idx] = lst[i]
        else:
            break
    stack.append(i)

print(*result)