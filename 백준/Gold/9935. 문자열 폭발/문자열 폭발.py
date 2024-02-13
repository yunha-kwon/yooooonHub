import sys
input = sys.stdin.readline
string = list(input().strip())
bomb = list(input().strip())
bomb_len = len(bomb)
stack = []

for i in string:
    stack.append(i)
    if stack[len(stack)-bomb_len:len(stack)] == bomb:
        for _ in range(bomb_len):
            stack.pop()

if stack:
    print(*stack, sep='')
else:
    print('FRULA')