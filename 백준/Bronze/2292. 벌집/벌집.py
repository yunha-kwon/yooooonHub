N = int(input())
s = 1
cnt = 1

while N > s:
    s += 6 * cnt
    cnt += 1

print(cnt)