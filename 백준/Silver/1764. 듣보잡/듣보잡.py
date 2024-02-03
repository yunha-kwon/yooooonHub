import sys
input = sys.stdin.readline

N, M = map(int, input().split())

not_listen = set()

for _ in range(N):
    not_listen.add(input().strip())

result = []

for _ in range(M):
    name = input().strip()
    if name in not_listen:
        result.append(name)

print(len(result))
result.sort()
print(*result, sep='\n')