n = int(input()) # 256
result = 0
for i in range(1, n+1):
    num = list(map(int, str(i))) #[2, 5, 6]
    if n == sum(num) + i:  #2+5+6 + (1~256)
        result = i
        break

print(result)
