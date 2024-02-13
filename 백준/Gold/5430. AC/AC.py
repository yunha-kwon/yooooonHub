from collections import deque

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    data = input()[1:-1].split(',')
    q = deque(data)

    if n == 0 :
        q = []

    reverse = 0
    flag = 0
    for value in p:
        if value == 'R':
            reverse += 1
        elif value == 'D':
            if q:
                if reverse % 2 == 0 : # 그대로
                    q.popleft()
                else: # 거꾸로
                    q.pop()
            else:
                flag = 1
                print('error')
                break

    if flag == 0 :
        if reverse % 2 == 0 : # 그대로
            print('[' + ','.join(q) + ']')
        else: # 거꾸로
            q.reverse()
            print('[' + ','.join(q) + ']')