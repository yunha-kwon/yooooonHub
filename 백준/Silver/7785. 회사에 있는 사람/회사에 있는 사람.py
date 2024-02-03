import sys
input = sys.stdin.readline

N = int(input())

dic = {}
for i in range(N):
    name, state = input().split()
    dic[name] = state

enter = []

for key, value in dic.items():
    if value == 'enter':
        enter.append(key)

enter.sort(reverse=True)
print(*enter, sep='\n')