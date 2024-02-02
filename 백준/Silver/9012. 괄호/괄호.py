# 괄호
T = int(input())

for _ in range(T):
    stack = []
    s = list(map(str, input()))
    # (가 나오면 그 개수만큼의 )가 있어야 함.
    VPS_check = True

    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                VPS_check = False
                break

    if not stack and VPS_check:
        print('YES')
    elif stack or not VPS_check:
        print('NO')
