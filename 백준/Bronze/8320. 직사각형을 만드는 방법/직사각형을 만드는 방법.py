n = int(input())
result = 0
for i in range(1, n+1):
    for j in range(i, n//i+1):
        result += 1

print(result)