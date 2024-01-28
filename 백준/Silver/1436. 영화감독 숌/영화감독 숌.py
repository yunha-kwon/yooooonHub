N = int(input())
i = 0
lst = []
while len(lst) < N:
    i += 1
    if '666' in str(i):
        lst.append(i)

print(lst[-1])