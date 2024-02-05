K = int(input())
stk = []

for _ in range(K):
    n = int(input())

    if n != 0:
        stk.append(n)
    elif n == 0:
        stk.pop()

print(sum(stk))