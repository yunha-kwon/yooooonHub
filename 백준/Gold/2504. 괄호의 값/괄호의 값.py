s = list(input())
stack = []
result = 0
cnt = 1

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
        cnt *= 2
    elif s[i] == '[':
        stack.append(s[i])
        cnt *= 3
    elif s[i] == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break
        if s[i-1] == '(':
            result += cnt
        stack.pop()
        cnt /= 2
    elif s[i] == ']':
        if not stack or stack[-1] == '(':
            result = 0
            break
        if s[i-1] == '[':
            result += cnt
        stack.pop()
        cnt /= 3

if stack:
    print(0)
else:
    print(int(result))

