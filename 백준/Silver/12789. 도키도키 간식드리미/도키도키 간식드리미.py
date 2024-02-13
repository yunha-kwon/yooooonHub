import sys

N = int(input())
num = list(map(int, sys.stdin.readline().split()))

stack = []
cnt = 1

while num:
    if cnt == num[0]:
        cnt += 1
        num.pop(0)
    
    else:
        stack.append(num.pop(0))

    while stack:
        if stack[-1] == cnt:
            stack.pop()
            cnt += 1
        
        else:
            break

if stack:
    print("Sad")
    
else:
    print("Nice")