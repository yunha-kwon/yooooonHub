n = int(input())
lst = [0, 1]

for i in range(n):
        lst.append((lst[i] + lst[i+1]) % 1000000007)

print(lst[n])